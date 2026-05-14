import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning
from sympy import im

warnings.filterwarnings(
    "ignore",
    category=LangChainPendingDeprecationWarning
)

from httpx import get
from langchain.agents import create_agent, AgentState
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from langchain.agents.middleware import before_agent,after_agent,before_model,after_model,wrap_model_call,wrap_tool_call
from langgraph.runtime import Runtime

@tool(description="查询天气,输入城市名称字符串，返回天气情况字符串")
def get_weather(city:str)->str:
    return f"{city}天气：晴天"

"""
    1.agent执行前
    2.agent执行后
    3.model执行前
    4.model执行后
    5.工具执行中
    6.模型执行中
"""

@before_agent
def log_before_agent(state:AgentState,runtime:Runtime)->None:
    #agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before_agent]agent启动，并附带{len(state['messages'])}消息")

@after_agent
def log_after_agent(state:AgentState,runtime:Runtime)->None:
    print(f"[after_agent]agent结束，共处理{len(state['messages'])}消息")

@before_model
def log_before_model(state:AgentState,runtime:Runtime)->None:
    print(f"[before_model]模型即将调用，当前消息{len(state['messages'])}消息")

@after_model
def log_after_model(state:AgentState,runtime:Runtime)->None:
    print(f"[after_model]模型调用结束，当前消息{len(state['messages'])}消息")

@wrap_model_call
def model_call_hook(request,handler):
    print("模型调用啦")
    return handler(request)

@wrap_tool_call
def monitor_tool(request,handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")
    return handler(request)


agent = create_agent(
    model = ChatTongyi(model="qwen3-max"),      #智能体的大脑
    tools = [get_weather],      #智能体的工具箱
    middleware=[log_before_agent,log_after_agent,log_before_model,log_after_model,model_call_hook,monitor_tool],   #智能体的中间件，可以在agent执行前后，模型调用前后，工具调用前后执行一些自定义逻辑
)

res = agent.invoke(
    {
        "messages":[
            {"role":"user","content":"深圳今天的天气如何？如何穿衣？"}
        ]
    }
)
print("***************\n",res)

