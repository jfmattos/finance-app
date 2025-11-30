#basemodel é a classe base do pydantic que vai ser usada para criar modelos
#de dados (schemas) e conseguir definir os atributos de cada classe
from pydantic import BaseModel


#definindos os tipos de cada item da minha compra do cartão(transação)
#esse e o formato da transação que vai retornar na API
class Transaction(BaseModel):
    id: int
    description: str
    category: str
    amount: float
