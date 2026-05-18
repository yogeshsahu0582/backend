from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.booking_model import Booking

from app.schemas.booking_schema import (
    BookingCreate
)

from app.services.socket_manager import (
    manager
)

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.post("/create")
async def create_booking(
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

    await manager.broadcast({

        "type": "new_booking",

        "booking_id":
            new_booking.id,

        "service_type":
            new_booking.service_type,

        "status":
            new_booking.status
    })

    return {
        "message":
            "Booking created",

        "booking_id":
            new_booking.id
    }


@router.get("/pending")
def pending_bookings(
    db: Session = Depends(get_db)
):

    bookings = db.query(Booking).filter(
        Booking.status == "pending"
    ).all()

    return bookings


@router.put("/accept/{booking_id}")
async def accept_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.status = "accepted"

    db.commit()

    await manager.broadcast({

        "type": "booking_accepted",

        "booking_id":
            booking.id,

        "status":
            booking.status
    })

    return {
        "message":
            "Booking accepted"
    }


@router.put("/reject/{booking_id}")
async def reject_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking.status = "rejected"

    db.commit()

    await manager.broadcast({

        "type": "booking_rejected",

        "booking_id":
            booking.id,

        "status":
            booking.status
    })

    return {
        "message":
            "Booking rejected"
    }


@router.get("/status/{booking_id}")
def booking_status(
    booking_id: int,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "booking_id":
            booking.id,

        "status":
            booking.status
    }