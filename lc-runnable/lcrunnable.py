from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# prompt
prompt = PromptTemplate(
    input_variables=["country"],
    template="What is the capital of {country}?"
)

# chain
chain = prompt | model

# user input
country = input("Enter a country: ")

# run
response = chain.invoke({"country": country})

print("Answer:", response.content)