from pydantic import BaseModel

class ShippingRequest(BaseModel):
    order_id: str
    address: str

class ShippingResponse(BaseModel):
    shipment_id: str
    status: str
    address: str
