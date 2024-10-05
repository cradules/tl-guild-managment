from sqlalchemy.orm import Session
from . import models, schemas


def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(name=player.name, role_id=player.role_id)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
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
