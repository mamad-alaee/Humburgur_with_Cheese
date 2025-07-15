from fastapi import FastAPI
from initiators.init_db import connect_to_db
from initiators.setRoutes import setRouters

originalApp = FastAPI(
    title="Humburgur with Cheese",
    description="A simple API for serving Humburgur with Cheese",
    version="0.1.0"
)

connect_to_db()
setRouters(originalApp)

