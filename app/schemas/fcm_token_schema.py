from pydantic import BaseModel

class FCMTokenCreate(BaseModel):

    user_type: str

    user_id: int

    fcm_token: str