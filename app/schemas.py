from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from .models import OrderType, OrderStatus

class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    quantity: int = 0

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class OrderBase(BaseModel):
    order_number: str
    order_type: OrderType
    product_id: int
    quantity: int
    total_cost: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: OrderStatus
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ShipmentBase(BaseModel):
    order_id: int
    origin: str
    destination: str
    estimated_arrival: Optional[datetime] = None

class ShipmentCreate(ShipmentBase):
    pass

class Shipment(ShipmentBase):
    id: int
    status: str
    model_config = ConfigDict(from_attributes=True)
