from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

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

    else:

        existing = Location(
            worker_id=location.worker_id,
            latitude=location.latitude,
            longitude=location.longitude
        )

        db.add(existing)

    db.commit()

    return {
        "message": "Location updated"
    }