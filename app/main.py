from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator
from . import crud, models, schemas
from .database import engine, get_db
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TradeFlow API", version="1.0.0")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"app": "TradeFlow", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/", response_model=list[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

@app.post("/shipments/", response_model=schemas.Shipment)
def create_shipment(shipment: schemas.ShipmentCreate, db: Session = Depends(get_db)):
    return crud.create_shipment(db=db, shipment=shipment)

@app.get("/stress")
def stress_test():
    start_time = time.time()
    while time.time() - start_time < 60.0:
        pass
    return {"status": "CPU Stressed!"}
