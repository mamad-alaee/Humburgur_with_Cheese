from models.User import User
from fastapi import HTTPException

def save_user(userData):
    try:
        created_user = User(**dict(userData)).save()
        return {"job":"ok", "data":str(created_user)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))