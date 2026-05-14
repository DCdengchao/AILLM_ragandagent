import os,json
from langchain_core.messages import message_to_dict,messages_from_dict
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables.history import RunnableWithMessageHistory
#message_to_dict:单个消息对象（BaseMessage实例）->字典
#messages_from_dict:[字典，字典...]->[消息，消息...]
#AIMessage,HumanMessage,SystemMessage都是BaseMessage的子类

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id        #会话id
        self.storage_path = storage_path    #不同会话id的存储文件，所在的文件夹路径
        #完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)

        #确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self,messages):
        #Sequence序列，类似list
        all_messages = list(self.messages) #已有的消息列表
        all_messages.extend(messages) #新消息和已有的消息融合成一个list

        #将数据同步写入到本地文件中
        #类对象写入文件->一堆二进制
        #为了方便，可以将BaseMessage消息转为字典（借助json模块以json字符串写入文件）
        #官方为message_to_dict:单个消息对象（BaseMessage实例）->字典
        new_messages = []
        for message in all_messages:
            message_dict = message_to_dict(message)
            new_messages.append(message_dict)
        
        #将数据写入文件
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    @property       #装饰器，表示该方法可以通过成员属性的方式访问
    def messages(self):
        #当前文件：list[字典]
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self):
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)




model = ChatTongyi(model="qwen3-max")

# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history}，" \
#     "用户提问：{input}，请回答"
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题。对话历史：" ),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题：{input}"),
    ]
)

str_parser = StrOutputParser()  

#打印直观理解
def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser


#实现通过会话id获取InMemoryChatMessageHistory对象的函数
def get_history(session_id):
    return FileChatMessageHistory(session_id,"./chat_history")

#创建一个新的链，对原有链增强功能，自动附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain,     #被增强的原有chain
    get_history,    #通过会话id获取InMemoryChatMessageHistory对象
    input_messages_key="input", #表示用户输入在模板中的占位符
    history_messages_key="chat_history"   #表示历史消息在模板中的占位符  

)

if __name__ == "__main__":
    #固定格式：添加langchain的配置，为当前配置所属的session_id
    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }

    # res = conversation_chain.invoke(
    #     {"input": "小明有2个猫"},session_config
    # )
    # print("第一次执行：",res)

    # res = conversation_chain.invoke(
    #     {"input": "小刚有1只狗"},session_config
    # )
    # print("第二次执行：",res)

    res = conversation_chain.invoke(
        {"input": "总共多少个宠物?"},session_config
    )
    print("第三次执行：",res)

