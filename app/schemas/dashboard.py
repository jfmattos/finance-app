from pydantic import BaseModel
from typing import List

class CategorySummary(BaseModel):
    category: str
    amount: float


class DashboardSummary(BaseModel):
    year: int
    month: int
    total_spent: float
    by_category: List[CategorySummary]
