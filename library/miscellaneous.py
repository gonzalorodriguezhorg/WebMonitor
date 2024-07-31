from datetime import datetime
import pytz
import json
import hashlib 
from cryptography.fernet import Fernet 

"""
Esta función retorna la fecha y hora actual en formato ISO para
poder ser insertado en MongoDB
"""
def get_datetime_now(location="America/Mexico_City", flag ="iso"):
    d = datetime.now(tz=pytz.timezone(location))
    if flag=="iso":
        d_iso = d.isoformat()
    else:
        d_iso = d.strftime("%Y-%m-%d %H:%M:%S")
    return d_iso

def convert_to_json (data):
    try:
        json_data = json.dumps(data)
        json_data = json_data.replace("\'", "\"")
        return json_data
    except Exception as e:
        print (e)
        
def hash_password(password):
    salt = ""
    hased_password = hashlib.sha256(password.encode()).hexdigest()
    salted_password = hashlib.sha256((password + salt).encode()).hexdigest()
    
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d