from pydantic import BaseModel

class BookingCreate(BaseModel):

    user_id: int

    worker_id: int

    service_type: str


class BookingStatusUpdate(BaseModel):

    status: str