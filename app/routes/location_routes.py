from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from datetime import datetime

from app.database.deps import get_db

from app.models.location_model import Location

from app.schemas.location_schema import LocationUpdate

router = APIRouter(
    prefix="/locations",
    tags=["Locations"]
)

@router.post("/update")
def update_location(
    location: LocationUpdate,
    db: Session = Depends(get_db)
):

    existing = db.query(Location).filter(
        Location.worker_id == location.worker_id
    ).first()

    if existing:

        existing.latitude = location.latitude

        existing.longitude = location.longitude

        existing.updated_at = datetime.utcnow()

    else:

        existing = Location(
            worker_id=location.worker_id,
            latitude=location.latitude,
            longitude=location.longitude
        )

        db.add(existing)

    db.commit()

    return {
        "message": "Live location updated"
    }


@router.get("/worker/{worker_id}")
def worker_location(
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
        "worker_id": location.worker_id,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "updated_at": location.updated_at
    }