from fastapi import APIRouter,Request,File,UploadFile,HTTPException
from random import randint
import shutil
from os import getcwd,makedirs
from os.path import isdir

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
    
    
@fake_router.post("/upload_profile")
async def upload_profile(profile_pic:UploadFile=File(...)):
    if profile_pic.content_type not in ["image/jpeg", "image/png", "image/gif"]:
        raise HTTPException(status_code=415, detail="Unsupported file type")
    if profile_pic.size < 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large")
    save_path = f"{getcwd()}/public"
    if not isdir(save_path):
        makedirs(save_path)
    with open(f"{save_path}/{profile_pic.filename}", "wb") as buffer:
        shutil.copyfileobj(profile_pic.file, buffer)
   

    