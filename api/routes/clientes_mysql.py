
from fastapi import APIRouter, Depends, HTTPException
from config.mysql import SessionLocal, meta, engine
from crud.clientes_mysql import get_clientes, create_cliente, get_cliente_by_id, get_cliente_by_name
from sqlalchemy.orm import Session
from schemas.schemas_mysql import ClientesSchema, ClientesCreateSchema

meta.create_all(bind=engine)

clients = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@clients.get("/clientes", response_model=list[ClientesSchema], tags=["Clientes"])
def get_all_clients(db:Session= Depends(get_db)):
    clientes = get_clientes(db)
    return clientes

@clients.post("/cliente", response_model=ClientesSchema, tags=["Clientes"])
def add_client(client:ClientesCreateSchema, db: Session=Depends(get_db)):
    return create_cliente(db=db, cliente=client)

@clients.get("/cliente/id/{cliente_id}", response_model=ClientesSchema, tags=["Clientes"])
def get_client_by_id(client_id=int, db: Session=Depends(get_db)):
    db_cliente = get_cliente_by_id(db, cliente_id=client_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_cliente

@clients.get("/cliente/nombre/{cliente_name}", response_model=ClientesSchema, tags=["Clientes"])
def get_client_by_name(nombre_cliente=str, db: Session=Depends(get_db)):
    db_cliente = get_cliente_by_name(db, cliente_name=nombre_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_cliente