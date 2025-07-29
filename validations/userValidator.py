from pydantic import BaseModel,constr,EmailStr
from fastapi import HTTPException,Form


class userValidator(BaseModel):
    full_name: constr(min_length=2,max_length=50) # type:ignore
    password: constr(min_length=8,max_length=50) # type:ignore
    email: EmailStr
    
    
    
async def getUserData(
    full_name: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
):
    try:
        return userValidator(full_name=full_name,password=password,email=email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

