from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/players/", response_model=schemas.PlayerResponse)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

@router.get("/players/", response_model=List[schemas.PlayerResponse])
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_players(db=db, skip=skip, limit=limit)
