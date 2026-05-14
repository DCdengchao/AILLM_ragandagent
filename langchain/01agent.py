import warnings
from langchain_core._api.deprecation import LangChainPendingDeprecationWarning

warnings.filterwarnings(
    "ignore",
    category=LangChainPendingDeprecationWarning
)

from httpx import get
from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool


@tool(description="查询天气")
def get_weather()->str:
    return "晴天"
   
agent = create_agent(
    model = ChatTongyi(model="qwen3-max"),      #智能体的大脑
    tools = [get_weather],      #智能体的工具箱
    system_prompt="你是一个聊天助手，可以回答用户问题",
)

res = agent.invoke(
    {
        "messages":[
            {"role":"user","content":"明天深圳的天气如何？"}
        ]
    }
)

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)


