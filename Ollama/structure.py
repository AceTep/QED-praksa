from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
from typing import List, Optional

class Feature(BaseModel):
    name: str
    description: Optional[str] = None

class Car(BaseModel):
    make: str
    model: str
    year: int
    price: float
    features: List[Feature]

class Inventory(BaseModel):
    dealership_name: str
    location: str
    cars: List[Car]

parser = PydanticOutputParser(pydantic_object=Inventory)

prompt = PromptTemplate.from_template(
    """You are a structured data generator. Your task is to create a fictional car dealership inventory using realistic-sounding data.

Requirements:
- Generate one fictional dealership name and location.
- Include at least 2 different cars.
- Each car must include: make, model, year (int), price (float), and a list of features.
- Each feature should have a name, and optionally, a short description.

Output strictly in **valid JSON format**, matching this schema:
{format_instructions}

Do not include any extra explanation or notes—only return the JSON.
"""
).partial(format_instructions=parser.get_format_instructions())


llm = OllamaLLM(model="gemma3:4b", temperature=0)

chain = prompt | llm | parser
output = chain.invoke({})  

print(output.model_dump_json(indent=2))