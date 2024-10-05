import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the path for the SQLite database
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "guild_management.db")  # Use environment variable if defined, else default

# Create the engine for SQLite
DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for getting DB session in FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
