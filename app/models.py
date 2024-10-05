from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    join_date = Column(DateTime, default=datetime.utcnow)
    total_points = Column(Integer, default=0)

    # Relationships
    role = relationship("Role", back_populates="players")
    events = relationship("PlayerEvent", back_populates="player")


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    permissions = Column(String)  # This can store permissions as a comma-separated string

    # Relationships
    players = relationship("Player", back_populates="role")


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    event_type = Column(String)  # PvP, PvE, Raid, etc.
    date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="upcoming")  # Upcoming, completed, etc.

    # Relationships
    players = relationship("PlayerEvent", back_populates="event")


class PlayerEvent(Base):
    __tablename__ = "player_events"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    points_awarded = Column(Integer)
    participated = Column(Boolean, default=True)

    # Relationships
    player = relationship("Player", back_populates="events")
    event = relationship("Event", back_populates="players")