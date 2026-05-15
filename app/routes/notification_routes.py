from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.notification_model import Notification

from app.schemas.notification_schema import NotificationCreate

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.post("/create")
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):

    new_notification = Notification(
        user_type=notification.user_type,
        user_id=notification.user_id,
        title=notification.title,
        message=notification.message
    )

    db.add(new_notification)

    db.commit()

    return {
        "message": "Notification created"
    }


@router.get("/{user_type}/{user_id}")
def get_notifications(
    user_type: str,
    user_id: int,
    db: Session = Depends(get_db)
):

    notifications = db.query(
        Notification
    ).filter(
        Notification.user_type == user_type,
        Notification.user_id == user_id
    ).all()

    return notifications