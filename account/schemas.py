# schemas.py
from ninja import Schema
from typing import Optional
from datetime import datetime

class UserCreateSchema(Schema):
    username: str
    password: str
    email: Optional[str] = None
    mobile: Optional[str] = None
    alternate_mobile: Optional[str] = None
    role: Optional[str] = 'buyer'

class UserUpdateSchema(Schema):
    email: Optional[str] = None
    mobile: Optional[str] = None
    alternate_mobile: Optional[str] = None
    role: Optional[str] = None

class UserOutSchema(Schema):
    id: int
    username: str
    email: Optional[str] = None
    mobile: Optional[str] = None
    alternate_mobile: Optional[str] = None
    role: str
    created: datetime
    updated: datetime
