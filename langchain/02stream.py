import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning

warnings.filterwarnings(
    "ignore",
    category=LangChainPendingDeprecationWarning
)

from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool

@tool(description="查询股票价格，传入股票名称，返回字符串信息")
def get_price(name:str)->str:
    return f"股票{name}的价格是20元"

@tool(description="查询股票基本信息，传入股票名称，返回字符串信息")
def get_info(name:str)->str:
    return f"股票{name}的基本信息是：这是一个科技公司"



agent = create_agent(
    model = ChatTongyi(model="qwen3-max"),
    tools = [get_price, get_info],
    system_prompt="你是一个只能助手，可以回答股票相关问题，记住请告诉我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream(
    {"messages":[{"role":"user","content":"传智教育股价多少，并介绍一下"}]},
    stream_mode="values"
):
    latest_message = chunk["messages"][-1]

    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError as e:
        pass