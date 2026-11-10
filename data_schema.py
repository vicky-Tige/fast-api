from pydantic import BaseModel
from datetime import datetime

class ProductRequest(BaseModel):
    product_name: str
    buying_price:float
    selling_price:float
    
class ProductResponse(BaseModel):
    id:int
    user_id:int
    product_name:str
    buying_price:float
    selling_price:float
    created_at:datetime

   