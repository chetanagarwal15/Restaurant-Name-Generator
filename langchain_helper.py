from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1",
    model_name="llama-3.3-70b-versatile",
    temperature=0.6,
)

prompt1 = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

prompt2 = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest menu items for {restaurant_name}"
)

chain1 = prompt1 | llm
chain2 = prompt2 | llm

def generate_restaurant(cuisine):
    name = chain1.invoke({"cuisine": cuisine}).content.strip()
    menu = chain2.invoke({"restaurant_name": name}).content.strip()

    return {
        "restaurant_name": name,
        "menu_items": menu
    }
