from fastapi import APIRouter, UploadFile, File, Form
import shutil
from typing import List

from schemas import UploadVideo, GetVideo
video_router = APIRouter()
@video_router.post("/")
async def root(title:str = Form(...), description:str = Form(...), file:UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_name": file.filename, 'info': info}

@video_router.post("/image")
async def upload_image(files:List[UploadFile] = File(...)):
    for image in files:
        with open(f'{image.filename}', 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
    return {"file_name": 'good'}

@video_router.get("/video")
async def get_video():
    user = {'id': 25, 'name': 'Pipec'}
    video = {'title': 'test', 'desc':'Description'}
    return GetVideo(**user, **video)