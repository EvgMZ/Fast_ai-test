from email import message
from lib2to3.pytree import Base
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class UploadVideo(BaseModel):
    title:str
    description: str


class GetVideo(BaseModel):
    user: User 
    video: UploadVideo

class Message(BaseModel):
    message: str