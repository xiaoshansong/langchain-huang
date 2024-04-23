# If this is your first time using playwright, you'll have to install a browser executable.
# Running `playwright install` by default installs a chromium browser executable.
# playwright install chromium

# 设置OpenAIAPI密钥
from dotenv import load_dotenv
load_dotenv()

from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain import hub

async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
print(tools)

from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

# LLM不稳定，对于这个任务，可能要多跑几次才能得到正确结果
model = ChatOpenAI(temperature=0.5)

prompt = hub.pull("hwchase17/structured-chat-agent")

agent = create_structured_chat_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

async def main():
    response = await agent_executor.ainvoke({"input":"What are the headers on python.langchain.com?"})
    print(response)

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())