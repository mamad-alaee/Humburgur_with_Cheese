from models.User import User
from fastapi import HTTPException
from jose import jwt
from models.Role import Role
from initiators.init_env import load_jwt_key_env

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
    
async def create_access_token(userData):
    userData['_id'] = str(userData['_id'])
    userData['role'] = str(userData['role'])
    role_name = Role.objects(id=userData['role']).first().name
    userData['role_name'] = role_name
    key = await load_jwt_key_env()
    jwt_token = jwt.encode(userData,algorithm="HS256",key=key)
    return {"job":"ok","access_token":jwt_token}
    
async def decode_access_token(token):
    key = await load_jwt_key_env()
    user_data = jwt.decode(token,algorithms="HS256",key=key)
    return user_data

def check_is_owner(requested_user_data):
    if requested_user_data['role_name'] == 'owner':
        return True
    else:
        return False

def check_is_admin_or_higher(requested_user_data):
    if requested_user_data['role_name'] in ['owner',"admin"]:
        return True
    else:
        return False
