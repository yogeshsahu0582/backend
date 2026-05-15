from pydantic import BaseModel

class NotificationCreate(BaseModel):

    user_type: str

    user_id: int

    title: str

    message: str