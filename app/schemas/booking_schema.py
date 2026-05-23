from pydantic import BaseModel


class BookingCreate(BaseModel):

    user_phone: str

    service_type: str

    description: str

    duration: str

    location: str

    latitude: float

    longitude: float

    price: float


class BookingResponse(BaseModel):

    id: int

    user_phone: str

    worker_name: str | None

    service_type: str

    description: str

    duration: str

    location: str

    latitude: float

    longitude: float

    price: float

    status: str

    class Config:

        from_attributes = True