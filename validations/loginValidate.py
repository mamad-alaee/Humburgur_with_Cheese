from pydantic import BaseModel, EmailStr, validator
from fastapi import Form, HTTPException


class loginValidate(BaseModel):
    email: EmailStr
    password: str


def getLogindata(
        email: str= Form(...),
        password: str= Form(...)
):
    try:
        return loginValidate(email=email, password=password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    