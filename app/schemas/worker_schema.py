from pydantic import BaseModel

class WorkerCreate(BaseModel):
    name: str
    phone: str
    skill_type: str