from routes.userRouter import user_router



def setRouters(app):
    app.include_router(user_router)
