'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# https://serpapi.com/  注册
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv
load_dotenv()

# 加载所需的库
from langchain.agents import load_tools
from langchain.agents import AgentExecutor,create_react_agent
from langchain.agents import AgentType
from langchain_openai import OpenAI
from langchain import hub

# 初始化大模型
llm = OpenAI()

# 需要安装langchainhub  pip install langchainhub
prompt = hub.pull("hwchase17/react")

# 设置工具 search engine ：在 https://serpapi.com/ 上注册并获取API key
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 初始化Agent tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
agent = create_react_agent(tools=tools, llm=llm,prompt=prompt)
# ZERO_SHOT_REACT_DESCRIPTION 根据工具的描述和请求内容的来决定使用哪个工具（最常用）
# self-ask-with-search 此代理只使用一个工具: Intermediate Answer,
# 它会为问题寻找事实答案(指的非 gpt 生成的答案, 而是在网络中,文本中已存在的), 如 Google search API 工具

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({"input":"目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？"})