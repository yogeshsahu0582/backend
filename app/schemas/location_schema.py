from pydantic import BaseModel

class LocationUpdate(BaseModel):

    worker_id: int

    latitude: float

    longitude: float