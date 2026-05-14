from fastapi import FastAPI

from app.database.connection import Base, engine

from app.models.user_model import User
from app.models.worker_model import Worker
from app.models.booking_model import Booking

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PA Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "PA Backend Running Successfully"
    }