from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.deps import get_db

from app.models.booking_model import Booking
from app.models.worker_model import Worker

from app.schemas.booking_schema import BookingCreate

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.post("/create")
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    available_worker = db.query(
        Worker
    ).filter(
        Worker.is_online == True,
        Worker.is_busy == False,
        Worker.skill_type == booking.service_type
    ).first()

    if not available_worker:

        return {
            "message": "No available workers found"
        }

    available_worker.is_busy = True

    new_booking = Booking(
        user_id=booking.user_id,
        worker_id=available_worker.id,
        service_type=booking.service_type,
        status="accepted",
        assigned_at=datetime.utcnow()
    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return {
        "message": "Booking assigned successfully",
        "booking_id": new_booking.id,
        "worker_id": available_worker.id
    }


@router.put("/start/{booking_id}")
def start_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(
        Booking
    ).filter(
        Booking.id == booking_id
    ).first()

    if not booking:

        return {
            "message": "Booking not found"
        }

    booking.status = "in_progress"

    booking.start_time = datetime.utcnow()

    db.commit()

    return {
        "message": "Booking started"
    }


@router.put("/complete/{booking_id}")
def complete_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(
        Booking
    ).filter(
        Booking.id == booking_id
    ).first()

    if not booking:

        return {
            "message": "Booking not found"
        }

    booking.status = "completed"

    booking.end_time = datetime.utcnow()

    worker = db.query(
        Worker
    ).filter(
        Worker.id == booking.worker_id
    ).first()

    if worker:

        worker.is_busy = False

    db.commit()

    return {
        "message": "Booking completed"
    }


@router.get("/active")
def active_bookings(
    db: Session = Depends(get_db)
):

    bookings = db.query(
        Booking
    ).filter(
        Booking.status.in_(
            ["accepted", "in_progress"]
        )
    ).all()

    return bookings