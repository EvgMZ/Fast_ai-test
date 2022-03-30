from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from db import metadata, database
from ormar import Model, Integer, ModelMeta, String, DateTime, ForeignKey

class MainMata(ModelMeta):
    class Meta:
        metadata = metadata
        database = database

class User(BaseModel):
    class Meta(MainMata):
        tablename = "user"
    id: int = Integer(primary_key=True)
    username: str = String(max_length=100)



class Video(Model):
    class Meta(MainMata):
        tablename = "video"
    id: int = Integer(primary_key=True)
    title: int = String(max_length=50)
    description: str = String(max_length=500)
    file: str = String(max_length=1000)
    create_at: datetime = DateTime(default=datetime.now)
    user: Optional[User] = ForeignKey(User)
