from pydantic import BaseModel

class SOSCreate(BaseModel):

    booking_id: int

    triggered_by: str

    message: str