from fastapi import APIRouter
from app.schemas.dashboard import DashboardSummary, CategorySummary
#importando 

router = APIRouter(
    prefix = "/dashboard"
)

@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(year: int = 2025, month: int = 11) -> DashboardSummary:
    """
    Endpoint de exemplo que devolve um resumo fake de gastos do mês.
    No futuro, vamos buscar esses dados no banco.
    """

    fake_data = DashboardSummary(
        year=year,
        month=month,
        total_spent=3540.75,
        by_category=[
            CategorySummary(category="mercado", amount=1200.50),
            CategorySummary(category="restaurante", amount=800.00),
            CategorySummary(category="transporte", amount=300.25),
            CategorySummary(category="outros", amount=1240.00),
        ],
    )

    return fake_data
