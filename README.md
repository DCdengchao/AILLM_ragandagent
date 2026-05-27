# AILLM RAG & Agent — 大模型 RAG 与 Agent 应用实战

基于 LangChain + 阿里云 DashScope（通义千问）的大模型应用开发项目，涵盖从基础 API 调用到生产级 RAG 智能客服和 ReAct Agent 的完整实践。

## 项目结构

```
AILLM_ragandagent-main/
├── base/                    # 基础篇：OpenAI 兼容 API 调用入门
│   ├── 01testapikey.py      #   API 连通性测试 + 流式输出（含 reasoning_content）
│   ├── 02openai.py          #   非流式对话补全（system/user/assistant 角色）
│   ├── 03openaistream.py    #   流式对话补全
│   ├── 04openaihistory.py   #   多轮对话历史管理
│   └── 06json.py            #   JSON 序列化/反序列化基础
│
├── langchain/               # 进阶篇：LangChain 框架 29 讲
│   ├── 01agent.py           #   第一个 LangChain Agent（天气查询工具）
│   ├── 01cos.py             #   余弦相似度手写实现
│   ├── 02aliyun.py ~ 05chat.py        # ChatTongyi 模型调用、流式输出
│   ├── 03react.py           #   ReAct Agent（BMI 计算 + 工具调用）
│   ├── 07messim.py          #   消息序列化/反序列化
│   ├── 08embed.py           #   DashScope 文本嵌入模型
│   ├── 09prompt.py          #   PromptTemplate / ChatPromptTemplate
│   ├── 10fewshot.py         #   Few-shot 提示工程
│   ├── 12format.py ~ 19runlambda.py   # LCEL 链式调用、输出解析器、RunnableLambda
│   ├── 20mem.py             #   对话记忆（InMemoryChatMessageHistory）
│   ├── 21longmem.py         #   文件持久化对话历史
│   ├── 22csvload.py ~ 25textload.py   # 文档加载器（CSV/JSON/PDF/TXT）
│   ├── 26vectorst.py        #   内存向量存储
│   ├── 27outvector.py       #   向量检索输出
│   ├── 28vectorprom.py      #   RAG 链：检索 → 格式化 → 提示词 → 模型 → 解析
│   ├── 29runpass.py         #   完整 RAG 流水线（InMemoryVectorStore + RunnablePassthrough）
│   ├── chroma_db/           #   本地 Chroma 向量库
│   ├── chat_history/        #   对话历史持久化目录
│   └── data/                #   示例数据（CSV/JSON/PDF/TXT）
│
├── prorag/                  # 实战篇：RAG 智能客服系统（服装行业）
│   ├── app_qa.py            #   Streamlit 智能问答界面
│   ├── app_file_uploader.py #   Streamlit 知识库文件上传界面
│   ├── rag.py               #   RAG 服务：检索链 + 对话历史（LCEL 管道）
│   ├── knowledge_base.py    #   知识库服务：文档切片 + MD5 去重 + Chroma 入库
│   ├── vector_stores.py     #   Chroma 向量存储封装
│   ├── file_history_store.py #  文件持久化对话历史（BaseChatMessageHistory）
│   ├── config_data.py       #   全局配置（模型、切片参数、持久化路径）
│   ├── data/                #   知识库文档（尺码推荐/洗涤养护/颜色选择）
│   └── chroma_db/           #   持久化向量库
│
└── proagent/                # 实战篇：ReAct Agent 智能客服（扫地机器人）
    ├── app.py               #   Streamlit 智扫通机器人智能客服界面
    ├── agent/
    │   ├── react_agent.py   #   ReAct Agent 核心：工具 + 中间件 + 动态提示词
    │   └── tools/
    │       ├── agent_tools.py    # 7 个 LangChain @tool（RAG检索/天气/位置/报告生成）
    │       └── middleware.py     # 3 个中间件（工具监控/模型日志/动态提示词切换）
    ├── rag/
    │   ├── rag_service.py   #   RAG 摘要服务：检索 → 提示词模板 → 模型 → 解析
    │   └── vector_store.py  #   向量库服务：MD5 去重 + 文档分块 + Chroma 入库
    ├── model/
    │   └── factory.py       #   抽象工厂模式：ChatModel / Embeddings 单例
    ├── config/
    │   ├── agent.yml        #   Agent 外部数据路径配置
    │   ├── chroma.yml       #   Chroma 向量库配置（分块大小/K值/文件类型）
    │   ├── rag.yml          #   模型名称配置（qwen3-max / text-embedding-v4）
    │   └── prompts.yml      #   提示词文件路径配置
    ├── prompts/
    │   ├── main_prompt.txt  #   主系统提示词（55行 ReAct 思考准则 + 工具说明）
    │   ├── rag_summarize.txt #  RAG 摘要提示词
    │   └── report_prompt.txt #  报告生成提示词（Markdown 格式输出）
    ├── utils/
    │   ├── config_handler.py    # YAML 配置加载器
    │   ├── file_handler.py      # 文件操作（MD5/PDF加载/TXT加载）
    │   ├── logger_handler.py    # 日志系统（控制台 + 按日滚动文件）
    │   ├── path_tool.py         # 项目路径工具
    │   └── prompt_loader.py     # 提示词文件加载器
    ├── data/
    │   ├── external/records.csv # 121行模拟用户使用记录（10用户×12月）
    │   └── *.txt/*.pdf          # 扫地机器人知识库文档
    ├── logs/                #   运行日志
    └── chroma_db/           #   持久化向量库
```

## 技术栈

| 类别 | 技术 |
|------|------|
| **大模型** | 阿里云 DashScope 通义千问（`qwen3-max` / `qwen3.6-plus`） |
| **嵌入模型** | `text-embedding-v4` |
| **LLM 框架** | LangChain（LCEL / Agent / Tool / Middleware） |
| **向量数据库** | Chroma（本地持久化） |
| **Web UI** | Streamlit |
| **配置管理** | YAML + Python 配置类 |
| **文档加载** | PyPDF、TextLoader、CSVLoader、JSONLoader |
| **API 兼容** | OpenAI SDK → DashScope 兼容端点 |

## 快速开始

### 1. 环境准备

```bash
# Python 3.11+
pip install openai langchain langchain-community langchain-chroma langchain-core
pip install streamlit chromadb pypdf pyyaml numpy
pip install dashscope
```

### 2. 配置 API Key

```bash
export DASHSCOPE_API_KEY="your-api-key"
```

### 3. 运行示例

**基础 API 调用：**
```bash
cd base
python 01testapikey.py
```

**LangChain 教程（按编号循序渐进）：**
```bash
cd langchain
python 01agent.py      # 第一个 Agent
python 29runpass.py    # 完整 RAG 流水线
```

**RAG 智能客服（服装行业）：**
```bash
cd prorag
streamlit run app_qa.py             # 智能问答界面
streamlit run app_file_uploader.py  # 知识库管理界面
```

**ReAct Agent 智能客服（扫地机器人）：**
```bash
cd proagent
streamlit run app.py
```

## 核心特性

### 1. ReAct Agent（proagent）
- **思考→行动→观察→再思考** 的自主推理循环
- 7 个 LangChain `@tool` 工具：RAG 检索、天气查询、用户定位、报告生成等
- **动态提示词切换**：通过 `@dynamic_prompt` 中间件，根据运行时上下文（`context["report"]`）自动切换系统提示词与报告生成提示词
- **工具调用中间件**：`@wrap_tool_call` 监控工具执行，`@before_model` 记录模型调用日志
- 严格的**报告生成约束**：`fill_context_for_report` 作为必调用前置工具，确保 4 步固定流程

### 2. RAG 检索增强生成（prorag + proagent）
- 基于 Chroma 向量库的文档检索
- `RecursiveCharacterTextSplitter` 智能文本分块
- MD5 去重机制避免重复入库
- LCEL 链式管道：`检索 → 格式化 → 提示词模板 → 模型 → 解析`
- 支持 PDF / TXT 多格式文档

### 3. 对话记忆管理
- `RunnableWithMessageHistory` 自动管理多轮对话上下文
- 支持 `InMemoryChatMessageHistory`（内存）和 `FileChatMessageHistory`（文件持久化）
- 按 `session_id` 隔离不同用户的对话历史

### 4. 架构设计模式
- **抽象工厂模式**：`model/factory.py` 统一管理 ChatModel 和 Embeddings 实例（单例）
- **YAML 驱动配置**：proagent 模块通过 4 个 YAML 文件配置所有参数
- **中间件管道**：利用 LangChain Agent Middleware 实现关注点分离（监控/日志/提示词切换）

## 学习路径

```
base/ (API 基础)
  → langchain/01-05 (模型调用)
  → langchain/07-10 (消息/嵌入/提示词)
  → langchain/12-19 (LCEL 链/输出解析)
  → langchain/20-21 (对话记忆)
  → langchain/22-29 (文档加载 → 向量库 → RAG)
  → prorag/ (RAG 实战：智能客服)
  → proagent/ (Agent 实战：ReAct + RAG + 动态提示词)
```
