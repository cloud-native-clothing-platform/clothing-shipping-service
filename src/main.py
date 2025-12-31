from fastapi import FastAPI
from src.api.shipping import router as shipping_router

app = FastAPI(title="Clothing Shipping Service")

app.include_router(shipping_router, prefix="/shipping", tags=["Shipping"])

@app.get("/health")
def health():
    return {"status": "UP"}
