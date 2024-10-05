from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.get("/roles/", response_model=List[schemas.RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db=db)

@router.post("/players/{player_id}/assign-role/{role_id}", response_model=schemas.PlayerResponse)
def assign_role(player_id: int, role_id: int, db: Session = Depends(get_db)):
    return crud.assign_role_to_player(db=db, player_id=player_id, role_id=role_id)
