from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.location_model import Location

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/update")

def update_location(

    booking_id: int,

    worker_name: str,

    latitude: float,

    longitude: float,

    db: Session = Depends(get_db)
):

    location = db.query(
        Location
    ).filter(
        Location.booking_id == booking_id
    ).first()

    if location:

        location.latitude = latitude

        location.longitude = longitude

    else:

        location = Location(

            booking_id=booking_id,

            worker_name=worker_name,

            latitude=latitude,

            longitude=longitude
        )

        db.add(location)

    db.commit()

    return {
        "message":
            "Location updated"
    }


@router.get("/{booking_id}")

def get_location(

    booking_id: int,

    db: Session = Depends(get_db)
):

    location = db.query(
        Location
    ).filter(
        Location.booking_id == booking_id
    ).first()

    if not location:

        return {
            "message":
                "No location found"
        }

    return {

        "worker_name":
            location.worker_name,

        "latitude":
            location.latitude,

        "longitude":
            location.longitude,

        "status":
            location.status
    }