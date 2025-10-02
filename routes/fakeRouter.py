from fastapi import APIRouter,Request
from random import randint


fake_router = APIRouter()



@fake_router.post('/send_sms')
async def send_sms(request: Request, phone_number: str):
    code = str(randint(1000, 9999))
    await request.app.state.redis.set(phone_number, code,ex=2)
    return {"message": f"SMS with code {code} has been sent to {phone_number}"}

@fake_router.post("/verify_code")
async def verify_code(request: Request, phone_number: str, code: str):
    original_code = await  request.app.state.redis.get(phone_number)
    if original_code == code:
        return {"message": "Code is correct"}
    else:
        return {"message": "Code is incorrect"}
    
    
