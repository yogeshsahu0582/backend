from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.sos_model import SOSAlert

from app.schemas.sos_schema import SOSCreate

router = APIRouter(
    prefix="/sos",
    tags=["SOS"]
)

@router.post("/trigger")
def trigger_sos(
    sos: SOSCreate,
    db: Session = Depends(get_db)
):

    new_alert = SOSAlert(
        booking_id=sos.booking_id,
        triggered_by=sos.triggered_by,
        message=sos.message
    )

    db.add(new_alert)

    db.commit()

    return {
        "message": "SOS alert triggered"
    }


@router.get("/all")
def all_sos_alerts(
    db: Session = Depends(get_db)
):

    alerts = db.query(SOSAlert).all()

    return alerts