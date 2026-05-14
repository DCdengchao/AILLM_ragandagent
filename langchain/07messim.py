from langchain_community.chat_models import ChatTongyi
# 得到模型对象
model = ChatTongyi(model = "qwen3-max")

# 构造消息列表
messages = [
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，再写一首唐诗")
]

# 调用stream流式输出
res = model.stream(input=messages)

#打印结果
for chunk in res:
    print(chunk.content, end=" ", flush=True)




