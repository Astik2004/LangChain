from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

model = init_chat_model("gpt-5-nano")

messages = [
    SystemMessage("You are a Python expert."),
    HumanMessage("Explain recursion in simple terms.")
]

response = model.invoke(messages)
print(response)
