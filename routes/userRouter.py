from fastapi import APIRouter,Depends
from validations.userValidator import userValidator,getUserData
from controllers.userController import save_user

user_router = APIRouter()


@user_router.get('/users')
async def get_all_users():
    return {"message": "All users"}

@user_router.get('/users/{user_id}')
async def get_user(user_id: int):
    return {"message": f"User with id {user_id}"}

@user_router.post('/users')
async def create_user(userData:userValidator = Depends(getUserData)):
    return save_user(userData)
    

@user_router.put('/users/{user_id}')
async def update_user(user_id: int):
    return {"message": f"User with id {user_id} updated"}

@user_router.delete('/users/{user_id}')
async def delete_user(user_id: int):
    return {"message": f"User with id {user_id} deleted"}

@user_router.post("/users/reset-password")
async def reset_password():
    return {"message":"password reset"}