"""Shipping estimate and shipment tracking API starter."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4

app = FastAPI(title="Clothing Shipping Service", version="1.0.0")
class ShipmentRequest(BaseModel): order_id: str; postal_code: str = Field(min_length=5, max_length=10)
class Shipment(BaseModel): shipment_id: str; order_id: str; postal_code: str; status: str = "label_created"; estimated_days: int = 4
SHIPMENTS: dict[str, Shipment] = {}
@app.get("/health")
def health(): return {"status": "ok", "service": "shipping"}
@app.post("/shipments", response_model=Shipment, status_code=201)
def create_shipment(request: ShipmentRequest):
    shipment = Shipment(shipment_id=str(uuid4()), order_id=request.order_id, postal_code=request.postal_code)
    SHIPMENTS[shipment.shipment_id] = shipment
    return shipment
@app.get("/shipments/{shipment_id}", response_model=Shipment)
def get_shipment(shipment_id: str):
    if shipment_id not in SHIPMENTS: raise HTTPException(404, "Shipment not found")
    return SHIPMENTS[shipment_id]
