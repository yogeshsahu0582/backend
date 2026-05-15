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
        message=sos.message,
        emergency_level=sos.emergency_level,
        admin_notified=True,
        contacts_notified=True,
        police_alert_requested=True,
        status="active"
    )

    db.add(new_alert)

    db.commit()

    db.refresh(new_alert)

    return {
        "message": "HIGH PRIORITY SOS TRIGGERED",
        "alert_id": new_alert.id,
        "admin_alert": True,
        "emergency_contacts_alerted": True,
        "police_request_flagged": True
    }


@router.get("/all")
def all_sos_alerts(
    db: Session = Depends(get_db)
):

    alerts = db.query(
        SOSAlert
    ).all()

    return alerts


@router.put("/resolve/{alert_id}")
def resolve_sos(
    alert_id: int,
    db: Session = Depends(get_db)
):

    alert = db.query(
        SOSAlert
    ).filter(
        SOSAlert.id == alert_id
    ).first()

    if not alert:
        return {
            "message": "Alert not found"
        }

    alert.status = "resolved"

    db.commit()

    return {
        "message": "SOS resolved successfully"
    }