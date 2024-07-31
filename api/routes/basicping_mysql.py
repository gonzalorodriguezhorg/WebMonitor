from fastapi import APIRouter, Depends, HTTPException
from config.mysql import SessionLocal, meta, engine
from sqlalchemy.orm import Session
from crud.basicping_mysql import get_all_basicping_monitor, create_ping_monitor, get_ping_by_id, get_ping_by_client_id, get_ping_by_id_and_client, update_monitor_by_id
from schemas.schemas_mysql import BasicPingCreateSchema, BasicPingSchema
from pprint import pprint

meta.create_all(bind=engine)

ping_monitor = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@ping_monitor.get("/pingmonitor", response_model=list[BasicPingSchema], tags=["Basic PING Monitor"])
def get_all_basicping(db:Session= Depends(get_db)):
    basicping_monitors = get_all_basicping_monitor(db)
    return basicping_monitors

@ping_monitor.post("/pingmonitor", response_model=BasicPingSchema, tags=["Basic PING Monitor"])
def create_new_ping_monitor(basicping_mon:BasicPingCreateSchema, db: Session=Depends(get_db)):
    return create_ping_monitor(db=db, monitor=basicping_mon)

@ping_monitor.get("/pingmonitor/id/{ping_id}", response_model=BasicPingSchema, tags=["Basic PING Monitor"])
def get_ping_monitor_by_id(idmonitor=int, db: Session=Depends(get_db)):
    db_ping = get_ping_by_id(db, ping_id=idmonitor)
    if db_ping is None:
        raise HTTPException(status_code=404, detail="PING Monitor not found")
    return db_ping

@ping_monitor.get("/pingmonitor/id_client/{client_id}", response_model=list[BasicPingSchema], tags=["Basic PING Monitor"])
def get_all_ping_monitor_by_client(idclient=int, db: Session=Depends(get_db)):
    db_ping = get_ping_by_client_id(db, cliente_id=idclient)
    if db_ping is None:
        raise HTTPException(status_code=404, detail="PING Monitor not found")
    return db_ping

@ping_monitor.put("/pingmonitor/update", response_model= dict, tags=["Basic PING Monitor"])
def update_ping_by_id(id_ping: int, id_client:int ,ping_monitor: dict, db: Session=Depends(get_db)):
    db_monitor = get_ping_by_id_and_client(db, ping_id=id_ping, client_id=id_client)
    if db_monitor is None:
        raise HTTPException(status_code=404, detail="PING Monitor not found")
    db_monitor = update_monitor_by_id(db,ping_monitor,id=id_ping)
    return db_monitor