from langchain_community.llms.tongyi import Tongyi  
# 阿里云通义千问

model = Tongyi(model="qwen-max")

#调用invoke向模型提问
res = model.invoke(input = "你是谁呀能做什么？")

print(res)
