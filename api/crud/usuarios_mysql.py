from sqlalchemy.orm import Session
from models.mysqldb import usuarios
from schemas.schemas_mysql import UsuariosCreateSchema

import sys
sys.path.insert(1,"/Users/gonza/OneDrive/Documentos/Netheads/Proyectos/MonitorWeb/")
from library.miscellaneous import get_datetime_now, row2dict

def get_usuarios(db: Session, skip: int=0, limit: int=1000):
    return db.query(usuarios).all()

def create_usuario(db: Session, usuario: UsuariosCreateSchema):
    datetime = get_datetime_now(flag="mysql")
    db_usuario= usuarios(nombre_usuario=usuario.nombre_usuario, correo_usuario=usuario.correo_usuario, 
                         enabled_usuario=usuario.enabled_usuario,password_usuario=usuario.password_usuario, 
                         clientes_idclientes= usuario.clientes_idclientes, roles_idroles=usuario.roles_idroles, 
                         creacion_cuenta_usuario = datetime)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario_by_email(db: Session, correo_usuario:str):
    return db.query(usuarios).filter(usuarios.correo_usuario==correo_usuario).first()

def get_usuario_by_id(db: Session, idusuario:int):
    return db.query(usuarios).filter(usuarios.idusuarios==idusuario).first()

def get_usuario_by_name(db: Session, nombre_usuario:str):
    return db.query(usuarios).filter(usuarios.nombre_usuario==nombre_usuario).first()

def update_usuario_by_id(db: Session, data_actualizar:dict, id=int):
    db.query(usuarios).filter(usuarios.idusuarios==id).update(data_actualizar)
    db.commit()
    #return db.query(usuarios).filter(usuarios.idusuarios==id).first()
    query = db.query(usuarios).filter(usuarios.idusuarios==id).first()
    return row2dict(query)