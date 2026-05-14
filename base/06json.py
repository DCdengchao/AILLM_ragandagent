import json
d = {
    "name": "周杰伦",
    "age": 30,
    "gender": "男"
}
# 将Python对象转换为JSON字符串
print(str(d))
s = json.dumps(d,ensure_ascii=False)
print(s)

l = [
    {
        "name": "周杰伦",
        "age": 30,
        "gender": "男"
    },
    {
        "name": "蔡依林",
        "age": 32,
        "gender": "女"
    },
    {
        "name": "王力宏",
        "age": 32,
        "gender": "男"
    }
]

print(json.dumps(l,ensure_ascii=False))

json_str = '{"name": "周杰伦", "age": 30, "gender": "男"}'
json_arr_str = '[{"name": "周杰伦", "age": 30, "gender": "男"}, {"name": "蔡依林", "age": 32, "gender": "女"}, {"name": "王力宏", "age": 32, "gender": "男"}]'

# 将JSON字符串转换为Python对象
res_dict = json.loads(json_str)
print(res_dict,type(res_dict))

res_list = json.loads(json_arr_str)
print(res_list,type(res_list))