from app.models.chart_spec import ChartSpec


def generate_r(spec: ChartSpec) -> str:

    if spec.chart_type == "bar":
        return f"""
library(ggplot2)

ggplot(df, aes(x={spec.x}, y={spec.y})) +
    geom_col(fill="steelblue") +
    ggtitle("{spec.title}")
"""

    if spec.chart_type == "line":
        return f"""
library(ggplot2)

ggplot(df, aes(x={spec.x}, y={spec.y})) +
    geom_line() +
    ggtitle("{spec.title}")
"""

    if spec.chart_type == "scatter":
        return f"""
library(ggplot2)

ggplot(df, aes(x={spec.x}, y={spec.y})) +
    geom_point() +
    ggtitle("{spec.title}")
"""

    if spec.chart_type == "histogram":
        return f"""
library(ggplot2)

ggplot(df, aes(x={spec.x})) +
    geom_histogram()
"""

    if spec.chart_type == "pie":
        return f"""
library(ggplot2)

ggplot(df, aes(x="", y={spec.y}, fill={spec.x})) +
    geom_col(width=1) +
    coord_polar(theta="y")
"""

    raise ValueError("Tipo de gráfico não suportado")