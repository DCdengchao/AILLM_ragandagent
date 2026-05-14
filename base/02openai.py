from openai import OpenAI
#1. 获取cilent对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#2. 调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages = [
        {"role":"system","content":"你是一个python编程专家，并且话很少"},
        {"role":"assistant","content":"好的，我是编程专家，并且话很少，你要问什么？"},
        {"role":"user","content":"输出1-10的数字，使用python代码"}
    ]
)

#3. 处理结果
print(response.choices[0].message.content)
