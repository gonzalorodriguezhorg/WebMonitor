from fastapi import APIRouter, Response
from config.db import conn
from schemas.ping import pingEntity, pingsEntity
from models.ping import Ping
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

ping = APIRouter()

@ping.get('/allpings', tags=["Ping Monitor"])
def find_all_pings():
    return pingsEntity(conn.MonitorWeb.BasicPing.find())

@ping.post('/ping', tags=["Ping Monitor"])
def add_ping(ping: Ping):
    add_ping = dict(ping)
    id = conn.MonitorWeb.BasicPing.insert_one(add_ping).inserted_id
    pingdata = conn.MonitorWeb.BasicPing.find_one({"_id":id})
    return pingEntity(pingdata)

@ping.get('/ping/{id}', tags=["Ping Monitor"])
def get_one(id: str):
    return pingEntity(conn.MonitorWeb.BasicPing.find_one({"_id":ObjectId(id)}))

@ping.put('/ping/{id}', tags=["Ping Monitor"])
def update_one(id: str, ping: Ping):
    conn.MonitorWeb.BasicPing.find_one_and_update(
        {"_id":ObjectId(id)},{"$set":dict(ping)})
    return Response(status_code=HTTP_204_NO_CONTENT)
    
@ping.delete('/ping/{id}', tags=["Ping Monitor"])
def delete_one(id: str):
    pingEntity(conn.MonitorWeb.BasicPing.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
