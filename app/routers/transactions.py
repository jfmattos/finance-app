#httpexception will return error messages
from fastapi import APIRouter, HTTPException

#will return a list of transactions
from typing import List

#importing the data from each transaction
from app.schemas.transaction import Transaction, TransactionCreate

#creating the route to transactions
router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],     # organizing /docs
)

#creating functions to manipulate the transactions
#response_model will validate the list format
#list_transactions will show them like an index page
@router.get("/", response_model=List[Transaction])
def list_transactions():
    #creating a fake list of transactions to test the API
    #each item its an object Transaction that pydantic will convert to JSON
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

    return fake_transactions


#this will get one specific transaction similar to a show function
@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int)  -> Transaction: #converting to integer

    # Lista fake, igual na list_transactions.
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

   #finding the transaction by the id
    for t in fake_transactions:
        if t.id == transaction_id:
            return t

    # if transaction id not found will show an error message (like activeRecord)
    raise HTTPException(status_code=404, detail="Transaction not found")

@router.post("/", response_model=Transaction)
def create_transaction(payload: TransactionCreate) -> Transaction:
    #will create a new trans. using the Transaction response and from the class TransactionCreate
    # using fake data for now
    fake_new_id = 99
    new_transaction = Transaction(
        id=fake_new_id,
        description=payload.description,
        amount=payload.amount,
        category=payload.category,
    )
    # FastAPI + Pydantic will convert to JSON
    return new_transaction
