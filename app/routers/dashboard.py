from fastapi import APIRouter

router = APIRouter(
    prefix = "/dashboard"
)


#testing with fake data
@router.get("/summary")
def get_dashboard_summary(year: int = 2025, month: int = 11):
    fake_data = {
        "year": year,
        "month": month,
        "total_spent": 3540.75,
        "by_category": [
            {"category": "mercado", "amount": 1200.50},
            {"category": "restaurante", "amount": 800.00},
            {"category": "transporte", "amount": 300.25},
            {"category": "outros", "amount": 1240.00},
        ],
    }
    return fake_data
