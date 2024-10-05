from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from . import models, schemas


def create_player(db: Session, player: schemas.PlayerCreate):
    # Check if player with the same name exists
    existing_player = db.query(models.Player).filter(models.Player.name == player.name).first()

    if existing_player:
        raise HTTPException(status_code=400, detail="Player with this name already exists.")

    db_player = models.Player(name=player.name, role_id=player.role_id, class_name=player.class_name)
    db.add(db_player)

    try:
        db.commit()
        db.refresh(db_player)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not create player due to a database error.")

    return db_player


def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()


def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(name=event.name, event_type=event.event_type, date=event.date)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Event).offset(skip).limit(limit).all()

