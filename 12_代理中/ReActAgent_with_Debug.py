'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import AgentExecutor,create_react_agent,load_tools

# 试一试LangChain的Debug和Verbose，看看有何区别
from langchain.globals import set_debug,set_verbose
set_debug(True)    # 开启Debug模式
set_verbose(True)  # 开启Verbose模式

from langchain_openai import OpenAI
from langchain import hub

# 配置日志输出，设置日志级别为DEBUG和输出位置为stdout
# 导入Python标准库中的logging模块，该模块提供了灵活的日志记录功能。
import logging
#导入Python标准库中的sys模块，sys模块提供了与Python解释器交互的功能。
import sys

# 使用logging模块的basicConfig方法配置日志记录。该方法用于配置根日志记录器，
# 以便定义日志记录的格式和行为。在此，设置了日志输出到标准输出流（sys.stdout），
# 并设置日志级别为DEBUG。这意味着所有DEBUG级别及以上的日志信息将被记录并输出到标准输出流。
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# 获取根日志记录器，并添加一个StreamHandler处理程序。
# StreamHandler是logging模块中用于将日志信息输出到流（例如sys.stdout）的处理程序。
# 通过将StreamHandler添加到根日志记录器中，可以确保所有的日志信息都输出到标准输出流。
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# openai.log = "debug"

# 初始化大模型
llm = OpenAI()

# 设置工具
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 需要安装langchainhub  pip install langchainhub
prompt = hub.pull("hwchase17/react")

# 初始化Agent
agent = create_react_agent(tools=tools, llm=llm,prompt=prompt)
# 跑起来
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input":"目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？"})