#basemodel é a classe base do pydantic que vai ser usada para criar modelos
#de dados (schemas) e conseguir definir os atributos de cada classe
from pydantic import BaseModel

# importando lista de objetos tipados
from typing import List

#definindo os tipos de cada atributo da classe CategorySummary
class CategorySummary(BaseModel):
    category: str
    amount: float


class DashboardSummary(BaseModel):
    year: int
    month: int
    total_spent: float
    by_category: List[CategorySummary]
