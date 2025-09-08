from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    username: str
    email: str
    user_type: str
    company_name: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    user_type: str
    company_name: str
    created_at: datetime
    
class ProductCreate(BaseModel):
    vendor_id: int
    name: str
    category: str
    price: float
    min_quantity: int
    stock: int

class ProductResponse(BaseModel):
    id: int
    vendor_id: int
    name: str
    category: str
    price: float
    min_quantity: int
    stock: int
    created_at: datetime

class OrderCreate(BaseModel):
    buyer_id: int
    total_amount: float
    discount_percent: float
    final_amount: float
    created_at: datetime

class OrderResponse(BaseModel):
    id: int
    buyer_id: int
    total_amount: float 

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

"""
Key Endpoints Detail
Calculate Discount (Most Important)
POST /orders/calculate
{
  "items": [
    {"product_id": 1, "quantity": 150},
    {"product_id": 2, "quantity": 75}
  ]
}

Response:
{
  "total_quantity": 225,
  "total_value": 2500.00,
  "discount_percent": 12,
  "discount_amount": 300.00,
  "final_amount": 2200.00,
  "breakdown": {
    "quantity_bonus": 5,
    "value_bonus": 3,
    "loyalty_bonus": 4
  }
}

Place Order
POST /orders
{
  "items": [
    {"product_id": 1, "quantity": 150},
    {"product_id": 2, "quantity": 75}
  ]
}
# Automatically applies discount and creates order
"""

class OrderCalculate(BaseModel):
    items: List[OrderItemCreate]

class OrderCalculateResponse(BaseModel):
    total_quantity: int
    total_value: float
    discount_percent: float
    discount_amount: float
    final_amount: float
    breakdown: dict

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    buyer_id: int
    total_amount: float
    discount_percent: float
    final_amount: float
    created_at: datetime    

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderItemCalculate(BaseModel):
    product_id: int
    quantity: int

class OrderItemCalculateResponse(BaseModel):
    unit_price: float
    subtotal: float 

class DiscountAlgorithm(BaseModel):
    buyer_id: int
    total_quantity: int
    total_value: float
    discount_percent: float

class DiscountAlgorithmResponse(BaseModel):
    discount_percent: float
    breakdown: dict

class DiscountAlgorithmCalculate(BaseModel):
    items: List[OrderItemCalculate]

class DiscountAlgorithmCalculateResponse(BaseModel):
    discount_percent: float
    breakdown: dict 
    
