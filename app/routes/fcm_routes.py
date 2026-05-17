from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.fcm_token_model import FCMToken

from app.schemas.fcm_token_schema import FCMTokenCreate

from app.services.firebase_service import (
    send_push_notification
)

router = APIRouter(
    prefix="/fcm",
    tags=["FCM Notifications"]
)

@router.post("/save-token")
def save_fcm_token(
    token_data: FCMTokenCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(
        FCMToken
    ).filter(
        FCMToken.user_id == token_data.user_id,
        FCMToken.user_type == token_data.user_type
    ).first()

    if existing:

        existing.fcm_token = token_data.fcm_token

    else:

        existing = FCMToken(
            user_type=token_data.user_type,
            user_id=token_data.user_id,
            fcm_token=token_data.fcm_token
        )

        db.add(existing)

    db.commit()

    return {
        "message": "FCM token saved"
    }


@router.post("/send")
def send_notification(
    token_data: FCMTokenCreate
):

    response = send_push_notification(
        token_data.fcm_token,
        "PA Notification",
        "New booking or SOS alert"
    )

    if response["success"]:

        return {
            "message": "Notification sent successfully",
            "firebase_response": response["response"]
        }

    else:

        return {
            "message": "Notification failed",
            "error": response["error"]
        }