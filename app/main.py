import uvicorn
from fastapi import FastAPI
from app.routers import players, events

app = FastAPI()

# Mount the routers
app.include_router(players.router, prefix="/api")
app.include_router(events.router, prefix="/api")

# Main function to run the server
def main():
    """Main entry point to run the FastAPI server."""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

# Run the server if this file is executed directly
if __name__ == "__main__":
    main()
