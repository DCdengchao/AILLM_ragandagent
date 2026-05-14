
md5_path = "./md5.text"

collection_name = "rag" #向量数据库的表名
persist_directory = "./chroma_db" #数据库本地存储文件夹

chunk_size = 1000 #文本分割的块大小
chunk_overlap = 100 #文本分割的重叠大小
separators = ["\n\n","\n",".","!","?","。","！","？"," ",""] #文本分割的分隔符列表，优先级从高到低

max_split_char_number = 1000

similarity_threshold = 1 #相似度阈值，超过这个值的文本才会被认为是相关的

embedding_model_name = "text-embedding-v4" #嵌入模型的名称，默认为text-embedding-v4，可以根据需要修改为其他模型
chat_model_name = "qwen3-max" #聊天模型的名称

session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    }

