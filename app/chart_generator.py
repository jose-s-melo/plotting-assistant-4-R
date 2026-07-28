import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

from prompt import chart_prompt
from app.models.chart_spec import ChartSpec

load_dotenv()

model: str = ""
temperature: float = 0.2
max_tokens: int = 800


llm = ChatMistralAI(
    model=model,
    max_tokens=max_tokens,
    temperature=temperature,
    api_key=os.getenv("MISTRAL_API_KEY")
)

structured_llm = llm.with_structured_output(ChartSpec)

chain = chart_prompt | structured_llm

def generate_chart(question: str):
    return chain.invoke(
        {
            "question": question
        }
    )