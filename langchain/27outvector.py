from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

#Chroma 向量数据库（轻量级的）
#确保langchain-chroma chromadb安装了

vector_store = Chroma(
    collection_name="test",   #当前向量存储起个名字，类似数据库的表名称
    embedding_function=DashScopeEmbeddings(),  #嵌入模型
    persist_directory="./chroma_db"   #指定数据存放的文件夹
)


loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source",     #指定本条数据的来源是哪里

)

documents = loader.load()

#向量存储的新增，删除，检索
vector_store.add_documents(
    documents=documents,    #被添加的文件,类型：List[Document]
    id=["id"+str(i) for i in range(1,len(documents)+1)] #给添加的文档提供id，类型：List[str]
)

#删除 传入[id,id,....]
vector_store.delete(ids=["id1","id2"])

#检索 返回类型：List[Document]
result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3,       #检索的结果要几个
    filter={"source":"黑马程序员"}  #过滤条件，指定来源是黑马程序员的文档
)

print(result)
