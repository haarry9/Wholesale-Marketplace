from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models import OrderCreate, OrderResponse, OrderItemCreate, OrderItemResponse, OrderCalculate, OrderCalculateResponse
from database import orders_collection, order_items_collection
from utils import get_current_user
from models import OrderCalculate, OrderCalculateResponse

router = APIRouter()

"""
POST /orders/calculate - Calculate discount for cart items
POST /orders - Place order with discount
GET /orders/my - Get user's orders
"""

"""
Discount Rules:
    1. Quantity Bonus: 100+ units = 5%, 500+ units = 10%, 1000+ units = 15%
    2. Value Bonus: $1000+ = 3%, $5000+ = 7%, $10000+ = 12%
    3. Loyalty Bonus: Previous orders count (1-3 orders = 2%, 4+ orders = 5%)

    Maximum discount: 25%
"""

@router.post("/calculate", response_model=OrderCalculateResponse)
async def calculate_order(order: OrderCalculate, current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "BUYER":
        raise HTTPException(status_code=403, detail="Forbidden")
    return calculate_order(order, current_user["id"])

@router.post("/", response_model=OrderResponse)
async def create_order(order: OrderCreate, current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "BUYER":
        raise HTTPException(status_code=403, detail="Forbidden")        
    return create_order(order, current_user["id"])

@router.get("/my", response_model=List[OrderResponse])
async def get_my_orders(current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "BUYER":
        raise HTTPException(status_code=403, detail="Forbidden")
    return get_my_orders(current_user["id"])

"""
def calculate_discount(buyer_id: int, total_quantity: int, total_value: float) -> float:
    ```
    Discount Rules:
    1. Quantity Bonus: 100+ units = 5%, 500+ units = 10%, 1000+ units = 15%
    2. Value Bonus: $1000+ = 3%, $5000+ = 7%, $10000+ = 12%
    3. Loyalty Bonus: Previous orders count (1-3 orders = 2%, 4+ orders = 5%)

    Maximum discount: 25%
    ```
    pass
"""
#complete the logic in the above fucntion
def calculate_discount(buyer_id: int, total_quantity: int, total_value: float) -> float:
    return calculate_discount(buyer_id, total_quantity, total_value)



@router.post("/calculate-discount", response_model=OrderCalculateResponse)
async def calculate_discount(discount:calculate_discount , current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "BUYER":
        raise HTTPException(status_code=403, detail="Forbidden")
    return calculate_discount(discount, current_user["id"])

