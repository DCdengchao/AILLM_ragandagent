from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser

#创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

#模型创建
model = ChatTongyi(model="qwen3-max",streaming=True)

#第一个提示词模板
first_prompt = PromptTemplate.from_template(
   "我邻居姓:{lastname},刚生了{gender},请起名," \
   "仅告知我名字无需其他内容，并且以json格式输出，json格式如下：{{\"name\":\"名字\"}}" \
   "请严格按照json格式输出，不要有其他内容"
)

#第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名:{name}，请帮我解析含义"
)

#构建链条
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({"lastname": "张", "gender": "女"})
# print(res)
# print(type(res))

for chunk in chain.stream({"lastname": "张", "gender": "女"}):
    print(chunk,end="",flush=True)