''' 在LangChain中，ConversationBufferMemory 是
用来存储对话历史信息的一种内存类型，它允许你保存对话上下文，
并在后续的交互中使用这些信息。以下是如何使用 ConversationBufferMemory 的一个例子：'''
# 从环境变量导入 API 密钥
from dotenv import load_dotenv
load_dotenv()

# 导入所需的库
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 初始化 ConversationBufferMemory 对象：
memory = ConversationBufferMemory()

# 初始化大语言模型
llm = OpenAI()

# 初始化对话链
#conversation = ConversationChain(
#    llm=llm,
#    memory=ConversationBufferMemory()
#)
conversation = ConversationChain(
    llm = llm,
    verbose = True,
    memory = memory
)

# 第一天的对话
# 回合1
conversation.predict(input="我姐姐明天要过生日，我需要一束生日花束。")
print("第一次对话后的记忆:",conversation.memory.buffer)

# 回合2
conversation("她喜欢粉色玫瑰，颜色是粉色的。")
print("第二次对话后的记忆:", conversation.memory.buffer)

# 回合3 （第二天的对话）
conversation("我又来了，还记得我昨天为什么要来买花吗？")
print("/n第三次对话后时提示:/n",conversation.prompt.template)
print("/n第三次对话后的记忆:/n", conversation.memory.buffer)

