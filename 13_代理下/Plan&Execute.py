# Plan-and-execute agents are planning tasks
# with a language model (LLM) and executing them with a separate agent.



# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv
load_dotenv()

from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain_openai import OpenAI,ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain.chains import LLMMathChain

llm = OpenAI()
search = SerpAPIWrapper()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]

model = ChatOpenAI()
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.invoke("在纽约，100美元能买几束玫瑰?")