from fastapi import APIRouter, Response
from config.db import conn
from schemas.dns import AdnsEntity, AdnsEntities, MXdnsEntities, MXdnsEntity, NSdnsEntities, NSdnsEntity, SOAdnsEntity, SOAdnsEntities, TXTdnsEntities, TXTdnsEntity
from models.dns import adns, mxdns, nsdns, soadns, txtdns
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

dns = APIRouter()

@dns.get('/alladnsrecords', tags=["DNS Monitor"])
def find_all_a_records():
    return AdnsEntities(conn.MonitorWeb.ADNS.find())

@dns.post('/adnsrecord', tags=["DNS Monitor"])
def add_adns(adns: adns):
    add_arecord = dict(adns)
    id = conn.MonitorWeb.ADNS.insert_one(add_arecord).inserted_id
    a_record_data = conn.MonitorWeb.ADNS.find_one({"_id":id})
    return AdnsEntity(a_record_data)

@dns.get('/allmxdnsrecords', tags=["DNS Monitor"])
def find_all_mx_records():
    return MXdnsEntities(conn.MonitorWeb.MXDNS.find())

@dns.post('/mxdnsrecord', tags=["DNS Monitor"])
def add_mxdns(mxdns: mxdns):
    add_mxrecord = dict(mxdns)
    id = conn.MonitorWeb.MXDNS.insert_one(add_mxrecord).inserted_id
    mx_record_data = conn.MonitorWeb.MXDNS.find_one({"_id":id})
    return MXdnsEntity(mx_record_data)

@dns.get('/allnsdnsrecords', tags=["DNS Monitor"])
def find_all_ns_records():
    return NSdnsEntities(conn.MonitorWeb.NSDNS.find())

@dns.post('/nsdnsrecord', tags=["DNS Monitor"])
def add_nsdns(nsdns: nsdns):
    add_nsrecord = dict(nsdns)
    id = conn.MonitorWeb.NSDNS.insert_one(add_nsrecord).inserted_id
    ns_record_data = conn.MonitorWeb.NSDNS.find_one({"_id":id})
    return NSdnsEntity(ns_record_data)

@dns.get('/allsoadnsrecords', tags=["DNS Monitor"])
def find_all_soa_records():
    return SOAdnsEntities(conn.MonitorWeb.SOADNS.find())

@dns.post('/soadnsrecord', tags=["DNS Monitor"])
def add_soadns(soadns: soadns):
    add_soarecord = dict(soadns)
    id = conn.MonitorWeb.SOADNS.insert_one(add_soarecord).inserted_id
    soa_record_data = conn.MonitorWeb.SOADNS.find_one({"_id":id})
    return SOAdnsEntity(soa_record_data)

@dns.get('/alltxtdnsrecords', tags=["DNS Monitor"])
def find_all_txt_records():
    return TXTdnsEntities(conn.MonitorWeb.TXTDNS.find())

@dns.post('/txtdnsrecord', tags=["DNS Monitor"])
def add_txtdns(txtdns: txtdns):
    add_txtrecord = dict(txtdns)
    id = conn.MonitorWeb.TXTDNS.insert_one(add_txtrecord).inserted_id
    txt_record_data = conn.MonitorWeb.TXTDNS.find_one({"_id":id})
    return TXTdnsEntity(txt_record_data)