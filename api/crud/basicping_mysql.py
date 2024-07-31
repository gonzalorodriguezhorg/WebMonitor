from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.mysqldb import basic_ping
from schemas.schemas_mysql import BasicPingCreateSchema

import sys
sys.path.insert(1,"/Users/gonza/OneDrive/Documentos/Netheads/Proyectos/MonitorWeb/")
from library.miscellaneous import get_datetime_now, row2dict

def get_all_basicping_monitor(db: Session, skip: int=0, limit: int=1000):
    return db.query(basic_ping).all()

def create_ping_monitor(db: Session, monitor: BasicPingCreateSchema):
    datetime = get_datetime_now(flag="mysql")
    db_pingmon= basic_ping(ip_domain=monitor.ip_domain, timeout=monitor.timeout, count=monitor.count, interval=monitor.interval, datetime_configuracion=datetime, datetime_ultima_modificacion= datetime, enabled_basic_ping=monitor.enabled_basic_ping, clientes_idclientes=monitor.clientes_idclientes)
    db.add(db_pingmon)
    db.commit()
    db.refresh(db_pingmon)
    return db_pingmon

def get_ping_by_id(db: Session, ping_id: int):
    return db.query(basic_ping).filter(basic_ping.idbasic_ping == ping_id).first()

def get_ping_by_client_id(db: Session, cliente_id: int):
    return db.query(basic_ping).filter(basic_ping.clientes_idclientes == cliente_id).all()

def get_ping_by_id_and_client(db: Session, ping_id: int, client_id:int):
    return db.query(basic_ping).filter(basic_ping.idbasic_ping == ping_id, basic_ping.clientes_idclientes==client_id).first()

def update_monitor_by_id(db: Session, data_actualizar:dict, id=int):
    db.query(basic_ping).filter(basic_ping.idbasic_ping==id).update(data_actualizar)
    db.commit()
    query = db.query(basic_ping).filter(basic_ping.idbasic_ping==id).first()
    return row2dict(query)