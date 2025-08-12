from models.User import User
from fastapi import HTTPException
from models.Role import Role
from controllers.authController import decode_access_token,check_is_owner,check_is_admin_or_higher

def save_user(userData):
    try:
        userData["role"] = Role.objects(name="customer").first()
        created_user = User(**userData).save()

        return {"job":"ok", "data":str(created_user)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

def delete_user_with_id(userId):
    deleted_user = User.objects(id=userId).delete()
    if deleted_user == 0:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"job":"ok", "data":f"user with id {userId} deleted successfully"}

def find_users(page,limit,jwt_token):
    if check_is_admin_or_higher(decode_access_token(jwt_token)):
        skip = (page-1)*limit
        userList = list(User.objects().skip(skip).limit(limit).as_pymongo())
        if len(userList) == 0:
            raise HTTPException(status_code=204, detail="No users found")
        else:
            for user in userList:
                user["_id"] = str(user["_id"])
                user["role"] = str(user["role"])
            return {"job":"ok", "data":userList}
    else:
        raise HTTPException(status_code=403, detail="You are not authorized to perform this action")
    
def find_user_with_id(userId):
    founded_user = list(User.objects(id=userId).as_pymongo())[0]
    if founded_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        founded_user["_id"] = str(founded_user["_id"])
        return {"job":"ok", "data":founded_user}
def update_user_with_id(userId, newUserData):
    founded_user = User.objects(id=userId).update(**newUserData)
    if founded_user == 0:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"job":"ok", "data":f"user with id {userId} updated successfully"}

def insert_admin_user(userData,token):
    try:
        requested_user_data = decode_access_token(token)
        userData["role"] = Role.objects(name="admin").first()
        if check_is_owner(requested_user_data):
            inserted_user = User(**userData).save()
            return {"job":"ok","message":"admin user created successfully"}
        else:
            raise HTTPException(status_code=403, detail="You are not authorized to perform this action")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    