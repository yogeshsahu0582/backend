from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.location_model import Location
from app.models.worker_model import Worker

from app.schemas.location_schema import LocationUpdate


router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)


# UPDATE WORKER LOCATION
@router.post("/update")
def update_location(
    location: LocationUpdate,
    db: Session = Depends(get_db)
):

    existing = db.query(Location).filter(
        Location.worker_id == location.worker_id
    ).first()

    # IF LOCATION EXISTS → UPDATE
    if existing:

        existing.latitude = location.latitude
        existing.longitude = location.longitude

    # ELSE → CREATE NEW LOCATION
    else:

        existing = Location(
            worker_id=location.worker_id,
            latitude=location.latitude,
            longitude=location.longitude
        )

        db.add(existing)

    db.commit()

    return {
        "message": "Location updated successfully"
    }


# TRACK WORKER LIVE LOCATION
@router.get("/track/{worker_id}")
def track_worker(
    worker_id: int,
    db: Session = Depends(get_db)
):

    location = db.query(Location).filter(
        Location.worker_id == worker_id
    ).first()

    if not location:

        return {
            "message": "Location not found"
        }

    return {
        "worker_id": worker_id,
        "latitude": location.latitude,
        "longitude": location.longitude
    }