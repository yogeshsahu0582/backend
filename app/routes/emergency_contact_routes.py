from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.emergency_contact_model import EmergencyContact

from app.schemas.emergency_contact_schema import EmergencyContactCreate

router = APIRouter(
    prefix="/emergency-contacts",
    tags=["Emergency Contacts"]
)

@router.post("/add")
def add_contact(
    contact: EmergencyContactCreate,
    db: Session = Depends(get_db)
):

    new_contact = EmergencyContact(
        user_id=contact.user_id,
        name=contact.name,
        phone=contact.phone,
        relation=contact.relation
    )

    db.add(new_contact)

    db.commit()

    db.refresh(new_contact)

    return {
        "message": "Emergency contact added"
    }


@router.get("/user/{user_id}")
def get_contacts(
    user_id: int,
    db: Session = Depends(get_db)
):

    contacts = db.query(
        EmergencyContact
    ).filter(
        EmergencyContact.user_id == user_id
    ).all()

    return contacts