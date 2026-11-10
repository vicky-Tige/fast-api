from fastapi import FastAPI,Depends
from data_schema import ProductRequest,ProductResponse
from model import Base, Product
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db,engine
Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def home():
     return {"message": "Welcome to Duka FastAPI"}

@app.post("/products",response_model=ProductResponse)
def create_product(prod : ProductRequest,
                   session:Session=Depends(get_db)):
     dbprod= Product(product_name=prod.product_name,
                     buying_price=prod.buying_price,
                     selling_price=prod.selling_price,
                     user_id=1)
     session.add(dbprod) 
     session.commit()

     return dbprod

@app.get("/products",response_model=list[ProductResponse])
def get_product( session:Session=Depends(get_db)):
     
            query=select(Product)
            products=session.scalars(query).all()

            return products
