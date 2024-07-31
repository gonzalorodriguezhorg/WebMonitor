from fastapi import APIRouter, Depends, HTTPException
from config.mysql import SessionLocal, meta, engine
from crud.usuarios_mysql import create_usuario, get_usuario_by_email, get_usuario_by_id, get_usuario_by_name, get_usuarios, update_usuario_by_id
from sqlalchemy.orm import Session
from schemas.schemas_mysql import UsuariosCreateSchema, UsuariosSchema

meta.create_all(bind=engine)

users = APIRouter()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@users.get("/usuarios", response_model=list[UsuariosSchema], tags=["Usuarios"])
def get_all_users(db:Session= Depends(get_db)):
    clientes = get_usuarios(db)
    return clientes

@users.post("/usuario", response_model=UsuariosSchema, tags=["Usuarios"])
def add_user(usuario:UsuariosCreateSchema, db: Session=Depends(get_db)):
    db_user = get_usuario_by_email(db, correo_usuario=usuario.correo_usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_usuario(db=db, usuario=usuario)

@users.get("/usuarios/id/{usuario_id}", response_model=UsuariosSchema, tags=["Usuarios"])
def get_user_by_id(idusuario=int, db: Session=Depends(get_db)):
    db_cliente = get_usuario_by_id(db, idusuario=idusuario)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_cliente

@users.post("/usuario/nombre/{nombre_usuario}", response_model=UsuariosSchema, tags=["Usuarios"])
def get_user_by_name(nombre_usuario=str, db: Session=Depends(get_db)):
    db_cliente = get_usuario_by_name(db, nombre_usuario=nombre_usuario)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_cliente

@users.post("/usuario/email/{correo_usuario}", response_model=UsuariosSchema, tags=["Usuarios"])
def get_user_by_email(mail_usuario=str, db: Session=Depends(get_db)):
    db_cliente = get_usuario_by_email(db, correo_usuario=mail_usuario)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_cliente

@users.put("/usuario/update/{id_usuario}", response_model= dict, tags=["Usuarios"])
def update_user_by_id(id_usuario: int, usuario: dict, db: Session=Depends(get_db)):
    db_id = get_usuario_by_id(db, idusuario = id_usuario)
    if db_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    if "correo_usuario" in  usuario:
        db_correo = get_usuario_by_email(db, usuario["correo_usuario"])
        if db_correo:
            raise HTTPException(status_code=404, detail="User's email already exists")
    db_usuario = update_usuario_by_id(db, data_actualizar=usuario, id=id_usuario)
    return db_usuario