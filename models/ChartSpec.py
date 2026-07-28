from pydantic import BaseModel
from typing import Literal, Optional

class ChartSpec(BaseModel):
    chart_type = Literal[
        "bar",
        "line",
        "scatter",
        "pie",
        "histogram"
    ]