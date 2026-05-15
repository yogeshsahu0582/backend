from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.booking_model import Booking

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

    new_booking = Booking(
        user_id=booking.user_id,
        worker_id=booking.worker_id,
        service_type=booking.service_type,
        status="pending"
    )

    db.add(new_booking)

    db.commit()

    db.refresh(new_booking)

    return {
        "message": "Booking created",
        "booking_id": new_booking.id
    }


@router.put("/accept/{booking_id}")
def accept_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        return {"message": "Booking not found"}

    booking.status = "accepted"

    db.commit()

    return {
        "message": "Booking accepted"
    }