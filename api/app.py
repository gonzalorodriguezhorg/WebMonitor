from fastapi import FastAPI
from routes.ping import ping
from routes.dns import dns
from routes.clientes_mysql import clients
from routes.usuarios_mysql import users
from routes.basicping_mysql import ping_monitor
app = FastAPI()

app.include_router(ping)
app.include_router(dns)
app.include_router(clients)
app.include_router(users)
app.include_router(ping_monitor)