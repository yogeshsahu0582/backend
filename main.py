from fastapi import FastAPI

from app.database.connection import Base, engine

from app.models.user_model import User
from app.models.worker_model import Worker
from app.models.booking_model import Booking
from app.models.location_model import Location
from app.models.sos_model import SOSAlert
from app.models.emergency_contact_model import EmergencyContact

from app.routes.user_routes import router as user_router
from app.routes.worker_routes import router as worker_router
from app.routes.auth_routes import router as auth_router
from app.routes.protected_routes import router as protected_router
from app.routes.location_routes import router as location_router
from app.routes.booking_routes import router as booking_router
from app.routes.sos_routes import router as sos_router
from app.routes.emergency_contact_routes import router as emergency_contact_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PA Backend",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(auth_router)
app.include_router(protected_router)
app.include_router(location_router)
app.include_router(booking_router)
app.include_router(sos_router)
app.include_router(emergency_contact_router)

@app.get("/")
def root():

    return {
        "message": "PA Backend Running Successfully"
    }