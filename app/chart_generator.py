import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

from app.prompt import chart_prompt
from app.models.chart_spec import ChartSpec

load_dotenv()

model: str = "ministral-3b-latest"
#model="ministral-3b-latest"
#model="ministral-8b-latest"
#model="mistral-small-latest"
#model="mistral-medium-latest"
#model="mistral-large-latest"


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

def generate_chart(question: str) -> ChartSpec:
    return chain.invoke(
        {
            "question": question
        }
    )