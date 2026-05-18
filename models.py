from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # dont need constructor if basemmodel is used, it will automatically create constructor for us
    
    # def __init__(self, id:int, name:str, description:str, price:int, quantity:int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity