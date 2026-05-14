from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max",streaming=True)

first_prompt = PromptTemplate.from_template(
    "我邻居姓:{lastname},刚生了{gender},请起名,仅告知我名字无需其他内容"
)

second_prompt = PromptTemplate.from_template(
    "姓名:{name}，请帮我解析含义"
)

#函数入参:AIMessage对象->dict对象
my_func = RunnableLambda(lambda ai_msg:{"name": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser 

for chunk in chain.stream({"lastname": "张", "gender": "女"}):
    print(chunk,end="",flush=True)