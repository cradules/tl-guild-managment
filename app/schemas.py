from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class PlayerCreate(BaseModel):
    name: str
    role_id: int

class PlayerResponse(BaseModel):
    id: int
    name: str
    total_points: int
    join_date: datetime

    class Config:
        orm_mode = True  # Allows ORM objects to be used directly in responses

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

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

class PlayerEventResponse(BaseModel):
    player_id: int
    event_id: int
    points_awarded: int

    class Config:
        orm_mode = True
