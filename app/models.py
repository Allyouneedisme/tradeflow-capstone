from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import enum

class OrderType(str, enum.Enum):
    IMPORT = "IMPORT"
    EXPORT = "EXPORT"

class OrderStatus(str, enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    sku = Column(String, unique=True, index=True, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    orders = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True, nullable=False)
    order_type = Column(Enum(OrderType), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    total_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    product = relationship("Product", back_populates="orders")
    shipments = relationship("Shipment", back_populates="order")

class Shipment(Base):
    __tablename__ = "shipments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    status = Column(String, default="PREPARING")
    estimated_arrival = Column(DateTime)
    order = relationship("Order", back_populates="shipments")
