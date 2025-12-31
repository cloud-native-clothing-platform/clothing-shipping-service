from fastapi import APIRouter
from src.models.schemas import ShippingRequest, ShippingResponse

router = APIRouter()

@router.post("/", response_model=ShippingResponse)
def create_shipment(req: ShippingRequest):
    return ShippingResponse(
        shipment_id="SHIP-001",
        status="CREATED",
        address=req.address
    )

@router.get("/{shipment_id}", response_model=ShippingResponse)
def get_shipment(shipment_id: str):
    return ShippingResponse(
        shipment_id=shipment_id,
        status="IN_TRANSIT",
        address="Bangalore, India"
    )
