from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from slowapi.errors import RateLimitExceeded

from slowapi.middleware import SlowAPIMiddleware

from slowapi.extension import _rate_limit_exceeded_handler

from app.database.connection import Base, engine

from app.middleware.limiter import limiter

from app.middleware.error_handler import global_exception_handler

from app.models.user_model import User
from app.models.worker_model import Worker
from app.models.booking_model import Booking
from app.models.location_model import Location
from app.models.sos_model import SOSAlert
from app.models.emergency_contact_model import EmergencyContact
from app.models.payment_model import Payment
from app.models.notification_model import Notification
from app.models.complaint_model import Complaint

from app.routes.user_routes import router as user_router
from app.routes.worker_routes import router as worker_router
from app.routes.auth_routes import router as auth_router
from app.routes.protected_routes import router as protected_router
from app.routes.location_routes import router as location_router
from app.routes.booking_routes import router as booking_router
from app.routes.sos_routes import router as sos_router
from app.routes.emergency_contact_routes import router as emergency_contact_router
from app.routes.payment_routes import router as payment_router
from app.routes.notification_routes import router as notification_router
from app.routes.complaint_routes import router as complaint_router
from app.routes.admin_routes import router as admin_router
from app.routes.live_routes import router as live_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PA Backend",
    version="1.0.0"
)

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_middleware(
    SlowAPIMiddleware
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(worker_router)
app.include_router(auth_router)
app.include_router(protected_router)
app.include_router(location_router)
app.include_router(booking_router)
app.include_router(sos_router)
app.include_router(emergency_contact_router)
app.include_router(payment_router)
app.include_router(notification_router)
app.include_router(complaint_router)
app.include_router(admin_router)
app.include_router(live_router)

@app.get("/")
def root():

    return {
        "message": "PA Backend Running Successfully"
    }