from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClientesBaseSchema(BaseModel):
    nombre_cliente: str
    monitores_disponibles: int
    planes_idplanes: int

class ClientesCreateSchema(ClientesBaseSchema):
    pass

class ClientesSchema(ClientesBaseSchema):
    idclientes: int
    class Config:
        orm_mode : True

class UsuariosBaseSchema(BaseModel):
    nombre_usuario: Optional[str] = Field(None, description="Username")
    correo_usuario: Optional[str] = Field(None, description="Username")
    enabled_usuario: Optional[bool] = Field(None, description="Username")

class UsuariosCreateSchema(UsuariosBaseSchema):
    password_usuario: Optional[str] = Field(None, description="Username")
    clientes_idclientes: Optional[int] = Field(None, description="")
    roles_idroles : Optional[int] = Field(None, description="")

class UsuariosSchema(UsuariosBaseSchema):
    idusuarios: Optional[int] = Field(None, description="")
    ultimo_acceso_usuario: Optional[datetime] = Field (None, description="Last time login user")
    creacion_cuenta_usuario : Optional[datetime] = Field(None, description="")
    class Config:
        orm_mode: True

class BasicPingBaseSchema(BaseModel):
    ip_domain : str
    timeout: int
    count: int
    interval: int
    enabled_basic_ping: bool
    datetime_ultima_modificacion: datetime
    
class BasicPingSchema(BasicPingBaseSchema):
    idbasic_ping: int

class BasicPingCreateSchema(BasicPingBaseSchema):
    clientes_idclientes: int
    datetime_configuracion: datetime