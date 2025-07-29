from routes.userRouter import user_router
from routes.authRouter import auth_router



def setRouters(app):
    app.include_router(user_router)
    app.include_router(auth_router)
