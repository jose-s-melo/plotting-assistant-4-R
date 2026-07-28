# Plotting Assistant 4 R

Assistente de IA desenvolvido com **LangChain** e **Mistral AI** capaz de interpretar solicitações em linguagem natural e convertê-las em especificações estruturadas de gráficos, que posteriormente podem ser transformadas em código **R (ggplot2)**.

## Objetivo

O projeto demonstra como utilizar um Large Language Model (LLM) para compreender a intenção do usuário e produzir uma representação estruturada de um gráfico, separando a etapa de interpretação da etapa de geração de código.

Exemplo:

**Entrada**

```text
Crie um gráfico de barras mostrando as vendas por estado.
```

**Saída**

```json
{
  "chart_type": "bar",
  "title": "Vendas por Estado",
  "x": "estado",
  "y": "vendas"
}
```

Essa estrutura pode então ser utilizada para gerar automaticamente código R utilizando **ggplot2**.

---

# Tecnologias

* Python
* LangChain
* Mistral AI

---

# Estrutura do projeto

```text
.
├── app
│   ├── models
│   ├── prompt.py
│   ├── chart_generator.py
│   └── r_generator.py
├── main.py
├── pyproject.toml
├── uv.lock
└── .env
```

---

# Pré-requisitos

* Python
* uv
* Uma chave da API da Mistral AI

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/jose-s-melo/plotting-assistant-4-R.git
cd plotting-assistant-4-R
```

Instale as dependências utilizando o **uv**:

```bash
uv sync
```

---

# Configuração

Crie um arquivo `.env` na raiz do projeto.

```env
MISTRAL_API_KEY=sua_api_key
```

---

# Executando

Execute o projeto com:

```bash
uv run python -m main
```

---

# Exemplo

Pergunta:

```text
Crie um gráfico de linhas mostrando a receita mensal.
```

Objeto retornado:

```python
ChartSpec(
    chart_type="line",
    title="Receita Mensal",
    x="mes",
    y="receita"
)
```

Código R gerado:

```r
library(ggplot2)

ggplot(df, aes(x = mes, y = receita)) +
    geom_line() +
    ggtitle("Receita Mensal")
```
