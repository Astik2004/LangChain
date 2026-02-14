from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate.from_template("Explain {topic} in detail")

prompt2 = PromptTemplate.from_template("Summarize this text in 3 lines:\n{text}")

chain=prompt1 | model | prompt2 | model

topic=input("Enter the topic: ")
response=chain.invoke({"topic": topic})
print(response.content)