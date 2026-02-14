from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=PromptTemplate(
    input_variables=["language","level"],
    template="Explain {language} in ten line for a {level} learner."
)

language=input("Enter the programming language: ")
level=input("Enter the learner level (beginner, intermediate, advanced): ")
response=model.invoke(prompt.format(language=language,level=level))
print(response.content)
