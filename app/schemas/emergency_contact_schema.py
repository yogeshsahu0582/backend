from pydantic import BaseModel

class EmergencyContactCreate(BaseModel):

    user_id: int

    name: str

    phone: str

    relation: str