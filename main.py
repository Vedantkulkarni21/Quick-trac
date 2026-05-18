from fastapi import FastAPI
from models import Product
from database import SessionLocal, engine
import database_models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "welcome to fastapi"

# since basemodel is used, we can directly create objects of product class without defining constructor
products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="budget lappie", price=9, quantity=1),
    Product(id=3, name="laptop", description="budget lappie", price=9, quantity=1),
    Product(id=4, name="laptop", description="budget lappie", price=9, quantity=1)
]

@app.get("/products")
def get_all_products():
    db = SessionLocal()
    products = db.query(database_models.Product).all()
    return products

@app.get("/products/{id}")
def get_spec_prod(id:int):
    db = SessionLocal();

    product = db.query(database_models.Product).filter(database_models.Product.id == id).first();

    if product:
        return product;
    
    return {"message": "product not found"}

@app.post("/products")
def add_product(product: Product):

    db = SessionLocal()

    db_product = database_models.Product(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(db_product)
    db.commit()
    return {"message": "Product added successfully"}

@app.put("/products/{id}")
def update_product(id:int, updated_product: Product):
    db = SessionLocal()

    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if(product):
        product.name = updated_product.name
        product.description = updated_product.description
        product.price = updated_product.price
        product.quantity = updated_product.quantity

        db.commit()
        return {"message": "Product updated successfully"}

    else:
        return {"message": "product not found"}

@app.delete("/products/{id}")
def delete_product(id:int):
    db = SessionLocal() 

    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if(product):
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}
        
    return {"message": "product not found"}  