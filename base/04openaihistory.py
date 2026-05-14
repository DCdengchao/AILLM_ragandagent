from openai import OpenAI
#1. 获取cilent对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#2. 调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages = [
        {"role":"system","content":"你是一个AI助理，回答很简洁"},
        {"role":"user","content":"小明有2条宠物狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有3只宠物猫咪"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"总共有几只宠物？"}
    ],
    stream=True #开启流式输出
)

#3. 处理结果
for chunk in response:
    if not chunk.choices:
        continue

    delta = chunk.choices[0].delta

    if delta.content is not None:
        print(delta.content, end=" ", flush=True)
print(" ")