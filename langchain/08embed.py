from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象，不传model默认用的是text-embedding-v1
model = DashScopeEmbeddings()

# 不用invoke和stream
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我讨厌你"]))
