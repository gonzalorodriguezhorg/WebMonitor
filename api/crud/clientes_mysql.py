from sqlalchemy.orm import Session
from models.mysqldb import Clientes
from schemas.schemas_mysql import ClientesCreateSchema

def get_clientes(db: Session, skip: int=0, limit: int=1000):
    return db.query(Clientes).all()

def create_cliente(db: Session, cliente: ClientesCreateSchema):
    db_cliente= Clientes(nombre_cliente=cliente.nombre_cliente, monitores_disponibles= cliente.monitores_disponibles, planes_idplanes= cliente.planes_idplanes )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_cliente_by_id(db: Session, cliente_id: int):
    return db.query(Clientes).filter(Clientes.idclientes == cliente_id).first()

def get_cliente_by_name(db: Session, cliente_name: str):
    return db.query(Clientes).filter(Clientes.nombre_cliente == cliente_name).first()