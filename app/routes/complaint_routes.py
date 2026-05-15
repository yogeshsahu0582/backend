from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.complaint_model import Complaint

from app.schemas.complaint_schema import ComplaintCreate

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)

@router.post("/create")
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    new_complaint = Complaint(
        booking_id=complaint.booking_id,
        raised_by=complaint.raised_by,
        complaint_message=complaint.complaint_message
    )

    db.add(new_complaint)

    db.commit()

    return {
        "message": "Complaint submitted"
    }


@router.get("/all")
def all_complaints(
    db: Session = Depends(get_db)
):

    complaints = db.query(
        Complaint
    ).all()

    return complaints


@router.put("/resolve/{complaint_id}")
def resolve_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:

        return {
            "message": "Complaint not found"
        }

    complaint.status = "resolved"

    db.commit()

    return {
        "message": "Complaint resolved"
    }