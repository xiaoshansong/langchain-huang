# 试一试LangChain的Debug和Verbose
from langchain.globals import set_debug,set_verbose
set_debug(True)    # 开启Debug模式
set_verbose(True)  # 开启Verbose模式
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import SerpAPIWrapper
from langchain_openai import OpenAI
# from langchain_community.chat_models import ChatAnthropic
from langchain.agents import (
    AgentExecutor, create_self_ask_with_search_agent,Tool
)
from langchain import hub

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()

tools = [
    Tool(
        name="Intermediate Answer", 
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

# model = ChatAnthropic()
# 需要安装langchainhub  pip install langchainhub
prompt = hub.pull("hwchase17/self-ask-with-search")

# 初始化Agent
agent = create_self_ask_with_search_agent(tools=tools, llm=llm,prompt=prompt)
# 跑起来
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,handle_parsing_errors=True)
agent_executor.invoke({"input":"使用玫瑰作为国花的国家的首都是哪里?"})