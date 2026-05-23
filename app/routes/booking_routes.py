from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.booking_model import Booking

from app.schemas.booking_schema import (
    BookingCreate
)

router = APIRouter(
    prefix="/booking",
    tags=["Booking"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/create")

def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db)
):

    new_booking = Booking(

        user_phone=booking.user_phone,

        service_type=booking.service_type,

        description=booking.description,

        duration=booking.duration,

        location=booking.location,

        latitude=booking.latitude,

        longitude=booking.longitude,

        price=booking.price
    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return {
        "message": "Booking Created",
        "booking_id": new_booking.id
    }


@router.get("/all")

def get_all_bookings(
    db: Session = Depends(get_db)
):

    bookings = db.query(
        Booking
    ).all()

    return bookings


@router.put("/accept/{booking_id}")

def accept_booking(
    booking_id: int,
    worker_name: str,
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

    booking.worker_name = worker_name

    booking.status = "accepted"

    db.commit()

    return {
        "message": "Booking accepted"
    }


@router.put("/reject/{booking_id}")

def reject_booking(
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

    booking.status = "rejected"

    db.commit()

    return {
        "message": "Booking rejected"
    }