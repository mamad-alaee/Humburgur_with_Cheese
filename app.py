from fastapi import FastAPI
from initiators.init_db import connect_to_db
from initiators.setRoutes import setRouters
from initiators.initData import init_base_data
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


originalApp = FastAPI(
    title="Humburgur with Cheese",
    description="A simple API for serving Humburgur with Cheese",
    version="0.1.0"
)

connect_to_db()
init_base_data()
setRouters(originalApp)


origins = [
    "varzesh3.ir"
]
originalApp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@originalApp.middleware("http")
async def filter_not_allowed_origins(request, call_next):
    try:
        origin = request.headers.get("origin")
        if origin in origins:
            res = call_next(request)
            return res
        else:
            return JSONResponse(status_code=403,
                                 content={"message": "Forbidden"})
    except Exception as e:
        return JSONResponse(status_code=500, 
                            content={"message": "Internal Server Error"})

@originalApp.middleware("http")
async def check_jwt_exist(request, call_next):
    try:
        token =request.headers.get("jwt-token")
        if token:
            res = call_next(request)
            return res
        else:
            return JSONResponse(status_code=401,
                                content={"message": "Unauthorized"})
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Internal Server Error"})