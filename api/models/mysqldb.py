from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from config.mysql import Base

class Clientes(Base):
    __tablename__= "clientes"
    idclientes = Column(Integer, primary_key=True)
    planes_idplanes = Column(Integer, ForeignKey("planes.idplanes"))
    nombre_cliente = Column(String(50), nullable=False)
    monitores_disponibles = Column (Integer, nullable=False)
    
class planes(Base):
    __tablename__ = "planes"
    idplanes = Column(Integer,primary_key=True)
    nombre_plan = Column(String(50))
    monitores_incluidos = Column(Integer)
    
class usuarios(Base):
    __tablename__ = "usuarios"
    idusuarios = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), nullable=False)
    correo_usuario = Column(String(50), nullable=False, unique=True)
    enabled_usuario = Column(Boolean, nullable=False)
    password_usuario = Column(String(255), nullable=False)
    ultimo_acceso_usuario = Column(DateTime, nullable=True)
    clientes_idclientes= Column(Integer, ForeignKey("clientes.idclientes"))
    roles_idroles = Column(Integer, ForeignKey("roles.idroles"))
    creacion_cuenta_usuario = Column(DateTime)
    
class roles(Base):
    __tablename__ = "roles"
    idroles = Column(Integer, primary_key=True)
    nombre_rol = Column(String(50), nullable=False)
    crear_monitor_rol = Column(Boolean)
    modificar_monitor_rol = Column(Boolean)
    ver_monitor_rol = Column(Boolean)
    crear_usuarios_rol = Column(Boolean)
    eliminar_usuarios_rol = Column(Boolean)
    modificar_plan_rol = Column(Boolean)
    eliminar_monitor_rol = Column(Boolean)
    
class basic_ping(Base):
    __tablename__ = "basic_ping"
    idbasic_ping = Column(Integer,primary_key=True)
    ip_domain = Column(String(100), nullable=False)
    timeout = Column(Integer)
    count = Column(Integer)
    interval = Column(Integer)
    enabled_basic_ping = Column(Boolean)
    datetime_configuracion = Column(DateTime)
    datetime_ultima_modificacion = Column(DateTime)
    clientes_idclientes = Column(Integer, ForeignKey("clientes.idclientes"))