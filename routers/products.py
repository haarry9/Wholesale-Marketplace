from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models import ProductCreate, ProductResponse
from database import products_collection
from utils import get_current_user

router = APIRouter()

"""
POST /products - Add product (vendors only)
GET /products - List all products
GET /products/{id} - Get product details
"""

@router.post("/", response_model=ProductResponse)
async def create_product(product: ProductCreate, current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "VENDOR":
        raise HTTPException(status_code=403, detail="Forbidden")
    product.vendor_id = current_user["id"]
    product = await products_collection.insert_one(product.model_dump())
    return ProductResponse(**product.model_dump())

@router.get("/", response_model=List[ProductResponse])
async def get_products(current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "VENDOR":
        raise HTTPException(status_code=403, detail="Forbidden")
    products = await products_collection.find({"vendor_id": current_user["id"]}).to_list(length=100)
    return [ProductResponse(**product) for product in products]

@router.get("/{id}", response_model=ProductResponse)
async def get_product(id: str, current_user: dict = Depends(get_current_user)):
    product = await products_collection.find_one({"id": id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse(**product)   

@router.put("/{id}", response_model=ProductResponse)
async def update_product(id: str, product: ProductCreate, current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "VENDOR":
        raise HTTPException(status_code=403, detail="Forbidden")
    product = await products_collection.find_one_and_update({"id": id}, {"$set": product.model_dump()})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse(**product)

@router.delete("/{id}", response_model=ProductResponse)
async def delete_product(id: str, current_user: dict = Depends(get_current_user)):
    if current_user["user_type"] != "VENDOR":
        raise HTTPException(status_code=403, detail="Forbidden")
    product = await products_collection.find_one_and_delete({"id": id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse(**product)
