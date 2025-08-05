from fastapi import APIRouter,Depends,Header
from validations.userValidator import userValidator,getUserData
from controllers.userController import insert_admin_user,update_user_with_id,find_user_with_id,find_users,save_user,delete_user_with_id

user_router = APIRouter()


@user_router.get('/users')
async def get_all_users(page:int=1,limit:int=10):
    return find_users(page,limit)

@user_router.get('/users/{user_id}')
async def get_user(user_id: str):
    return find_user_with_id(user_id)

@user_router.post('/users')
async def create_user(userData:userValidator = Depends(getUserData)):
    return save_user(dict(userData))
    

@user_router.put('/users/{user_id}')
async def update_user(user_id: str,userData:userValidator = Depends(getUserData)):
    return update_user_with_id(user_id,dict(userData))

@user_router.delete('/users/{user_id}')
async def delete_user(user_id: str):
    return delete_user_with_id(user_id)

@user_router.post("/admin")
async def create_admin_user(userData:userValidator = Depends(getUserData),jwt_token:str = Header(...)):
    return insert_admin_user(dict(userData),jwt_token)