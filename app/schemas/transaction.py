#basemodel é a classe base do pydantic que vai ser usada para criar modelos
#de dados (schemas) e conseguir definir os atributos de cada classe
from pydantic import BaseModel


#definindos os tipos de cada item da minha compra do cartão(transação)
#esse e o formato da transação que vai retornar na API

class TransactionBase(BaseModel): #atributes from incoming transaction
    description: str
    amount: float
    category: str

class TransactionCreate(TransactionBase): #creating the transaction from the TransactionBase (request/entrada)
    pass

class Transaction(TransactionBase): #will read and return to JSON now with the id (response/saida)
    id: int
