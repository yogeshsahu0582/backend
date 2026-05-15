from pydantic import BaseModel

class ComplaintCreate(BaseModel):

    booking_id: int

    raised_by: str

    complaint_message: str