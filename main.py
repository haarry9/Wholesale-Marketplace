from fastapi import FastAPI, APIRouter
from routers import auth, products, orders

app = FastAPI(title="Wholesale Marketplace")

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)
