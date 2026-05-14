from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

"""
PromptTemplate->StringPromptTemplate->BasePromptTemplate
FewShotPromptTemplate->StringPromptTemplate->BasePromptTemplate
ChatPromptTemplate->BaseChatPromptTemplate->BasePromptTemplate
"""

template = PromptTemplate.from_template("我的邻居是:{lastname},最喜欢:{hobby}")

res = template.format(lastname="张三", hobby="游泳")  # 我的邻居是:张三,最喜欢:游泳
print(res,type(res))

res2 = template.invoke({"lastname": "李四", "hobby": "跑步"})  # 我的邻居是:李四,最喜欢:跑步
print(res2,type(res2))


