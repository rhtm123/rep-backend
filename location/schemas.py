
from ninja import Schema
from typing import Optional
from datetime import datetime

from pydantic import Field


## city 
# schemas.py

class CityCreateSchema(Schema):
    name: str = Field(..., max_length=255) # 
    state_id: int

class CityUpdateSchema(Schema):
    name: Optional[str] = Field(None, max_length=255)
    state_id: Optional[int]

class CityOutSchema(Schema):
    id: int
    name: str
    state_id: int



