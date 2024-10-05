from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    event_type: str
    date: datetime

class EventResponse(BaseModel):
    id: int
    name: str
    event_type: str
    date: datetime

    class Config:
        orm_mode = True

class PlayerCreate(BaseModel):
    name: str
    role_id: Optional[int] = None
    class_name: str  # Player's weapon (class)

class PlayerResponse(BaseModel):
    id: int
    name: str
    role_id: int
    class_name: str
    total_points: int
    join_date: datetime

    class Config:
        orm_mode = True


class RoleCreate(BaseModel):
    name: str
    permissions: str

class RoleResponse(BaseModel):
    id: int
    name: str
    permissions: str

    class Config:
        orm_mode = True

