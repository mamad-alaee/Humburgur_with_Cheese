from fastapi import APIRouter,Depends,Header
from validations.loginValidate import loginValidate,getLogindata
from controllers.authController import login_with_email_and_password,decode_access_token
auth_router = APIRouter()



@auth_router.post('/login')
def login(loginData:loginValidate=Depends(getLogindata)):
    return login_with_email_and_password(dict(loginData))

@auth_router.post('/checkJwt')
def check_jwt(access_token:str=Header(...)):
    return decode_access_token(access_token)