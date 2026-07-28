from app.chart_generator import generate_chart
from app.r_generator import generate_r


question = """
Crie um gráfico de barras mostrando as vendas por estado.
"""

spec = generate_chart(question)

print("Especificação do gráfico: \n")
print(spec)

print()

print("Gráfico em R: \n")
print(generate_r(spec))