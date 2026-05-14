from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",", #指定分隔符为逗号
        "quotechar": '"', #指定带有分隔符文本的引号包围是单引号还是双引号
        #如果数据原来有表头，就不需要下面代码
        # "filednames": ["a","b","c","d"] 
    },
    encoding="utf-8" #指定编码为utf-8，避免中文乱码
)

#批量加载 load()->[Ducument,Document...]

# documents = loader.load()
# print(documents)

#懒加载 lazy_load()->迭代器
for document in loader.lazy_load():
    print(document)



