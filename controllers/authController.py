from models.User import User
from fastapi import HTTPException
from jose import jwt

def login_with_email_and_password(userData):
    founded_user = list(User.objects(email=userData['email']).as_pymongo())[0]
    if founded_user :
        if founded_user["password"] == userData['password']:
            return create_access_token(founded_user)
        else:
            raise HTTPException(status_code=401, detail="Invalid password")
    else:
        print("here")
        raise HTTPException(status_code=404, detail="User not found")
    
def create_access_token(userData):
    userData['_id'] = str(userData['_id'])
    jwt_token = jwt.encode(userData,algorithm="HS256",key="jamalzadeBacheKhoob")
    return {"job":"ok","access_token":jwt_token}
    
def decode_access_token(token):
    user_data = jwt.decode(token,algorithms="HS256",key="jamalzadeBacheKhoob")
    return user_data