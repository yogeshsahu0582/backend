from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.worker_model import Worker

from app.schemas.worker_schema import WorkerCreate

router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)

@router.post("/register")
def register_worker(
    worker: WorkerCreate,
    db: Session = Depends(get_db)
):

    new_worker = Worker(
        name=worker.name,
        phone=worker.phone,
        skill_type=worker.skill_type
    )

    db.add(new_worker)

    db.commit()

    db.refresh(new_worker)

    return {
        "message": "Worker Registered Successfully",
        "worker_id": new_worker.id
    }