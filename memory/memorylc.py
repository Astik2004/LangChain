from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant"),
    ("human","{input}")
])

chain = prompt | model

store = {}

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input"
)

while True:
    user = input("You: ")

    response = chatbot.invoke(
        {"input": user},
        config={"configurable": {"session_id": "user1"}}
    )

    print("AI:", response.content)
