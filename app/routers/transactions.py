from fastapi import APIRouter

#vamos retornar uma lista de transactions
from typing import List

#importando os dados de cada transaction
from app.schemas.transaction import Transaction

#aqui vamos criar todas as funções que vai manipular as transactions
router = APIRouter(
    prefix="/transactions",    # tudo aqui começa com /transactions
    tags=["transactions"],     # só pra organização na documentação /docs
)


@router.get("/", response_model=List[Transaction])
def list_transactions():
    #Lista transações (por enquanto, dados fake).
    #Em Rails seria a action index do TransactionsController:
    # Aqui criamos uma lista "fake" de transações só pra testar a API.
    # Cada item é um objeto Transaction, que o Pydantic sabe converter pra JSON.
    fake_transactions = [
        Transaction(
            id=1,
            description="Mercado Guanabara",
            amount=120.50,
            category="mercado",
        ),
        Transaction(
            id=2,
            description="Uber para o trabalho",
            amount=32.00,
            category="transporte",
        ),
        Transaction(
            id=3,
            description="Ifood jantar",
            amount=85.90,
            category="restaurante",
        ),
    ]

    # No FastAPI, só devolver a lista já é suficiente.
    # O response_model=List[Transaction] garante que o formato será validado.
    return fake_transactions
