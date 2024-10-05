from fastapi import FastAPI
from .routers import players, events

app = FastAPI()

# Mount the routers
app.include_router(players.router, prefix="/api")
app.include_router(events.router, prefix="/api")
