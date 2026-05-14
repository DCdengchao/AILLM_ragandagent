
#streamlit:当WEB页面发生变化，则代码重新执行一边

import streamlit as st
import time
from knowledge_base import KnowledgeBaseService


#添加网页标题
st.title("知识库更新服务")

#file_uploader
uploader_file = st.file_uploader(
    "请上传TXT文件",
    type=["txt"],
    accept_multiple_files=False,  #False表示只能上传一个文件，True表示可以上传多个文件
)
 
#session_state就是一个字典:当网页发生变化时，session_state中的数据不会丢失，可以用来保存一些状态信息
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService() #创建一个知识库服务的实例，保存在session_state中

if uploader_file is not None:
    #提取文件的信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size/1024

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size}")

    #get_value->bytes->decode
    text = uploader_file.getvalue().decode("utf-8")
    # st.write(text)

    with st.spinner("载入知识库中..."):         #在spinner内的代码执行过程中，会有一个转圈动画
        time.sleep(1) 
        result = st.session_state["service"].upload_by_str(text,file_name)
        st.write(result) 


        