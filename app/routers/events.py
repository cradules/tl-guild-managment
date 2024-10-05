from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from typing import List

router = APIRouter()

@router.post("/events/", response_model=schemas.EventResponse)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)

@router.get("/events/", response_model=List[schemas.EventResponse])
def get_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_events(db=db, skip=skip, limit=limit)
