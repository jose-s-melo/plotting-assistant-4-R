from langchain_core.prompts import ChatPromptTemplate

system_prompt = """
Você é um especialista em análise e visualização de dados.
Sua função é converter a solicitação em uma especificação de gráfico.
Os tipos de gráficos permitidos são:
- bar
- line
- scatter
- pie
- histogram

Nunca invente colunas.
Retorne apenas os campos necessários. 
"""

chart_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", system_prompt
        ),
        (
            "human", "{question}"
        )
    ]
)