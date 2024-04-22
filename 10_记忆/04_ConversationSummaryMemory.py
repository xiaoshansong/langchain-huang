'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI API密钥
from dotenv import load_dotenv
load_dotenv()
# 导入所需的库
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

# 初始化大语言模型
llm = OpenAI()

summary_memory = ConversationSummaryMemory(llm=llm)

# 初始化对话链
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=summary_memory
)

# 第一天的对话
# 回合1
result = conversation.predict(input="我姐姐明天要过生日，我需要一束生日花束。")
print(result)
# 回合2
result = conversation.predict(input="她喜欢粉色玫瑰，颜色是粉色的。")
# print("\n第二次对话后的记忆:\n", conversation.memory.buffer)
print(result)

# 第二天的对话
# 回合3
result = conversation.predict(input="我又来了，还记得我昨天为什么要来买花吗？")
print(result)

print(summary_memory.load_memory_variables({}))