import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager  # Ensure this import is here
from app.routers import players, events, roles
from app.database import engine, SessionLocal
from app import models

# Seed roles at startup
def seed_roles(db):
    roles = [
        {"name": "Guild Leader", "permissions": "manage_all"},
        {"name": "Officer", "permissions": "start_raid,manage_contracts"},
        {"name": "Advisor", "permissions": "advise_leader,assist_contracts"},
        {"name": "Veteran", "permissions": "lead_small_squad"},
        {"name": "Member", "permissions": ""},
        {"name": "Initiate", "permissions": ""},
    ]
    for role_data in roles:
        existing_role = db.query(models.Role).filter(models.Role.name == role_data["name"]).first()
        if not existing_role:
            role = models.Role(name=role_data["name"], permissions=role_data["permissions"])
            db.add(role)
    db.commit()

# Lifespan context manager for initializing the database and seeding roles
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)  # Initialize DB
    db = SessionLocal()
    seed_roles(db)  # Seed the roles
    db.close()
    yield  # FastAPI app runs here

# Initialize the FastAPI app with lifespan handling
app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(players.router, prefix="/api")
app.include_router(events.router, prefix="/api")
app.include_router(roles.router, prefix="/api")

# Main function to start the server using Uvicorn
def main():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
