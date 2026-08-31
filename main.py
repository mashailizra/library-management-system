from fastapi import FastAPI
from pydantic import BaseModel

from models import Library, Member


class MemberCreate(BaseModel):
    name: str
    age: int
    member_id: str
    membership_type: str

app = FastAPI()