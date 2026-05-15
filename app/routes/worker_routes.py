from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.worker_model import Worker

from app.schemas.worker_schema import WorkerCreate

router = APIRouter(
    prefix="/workers",
    tags=["Workers"]
)

# ---------------- REGISTER WORKER ---------------- #

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


# ---------------- GO ONLINE ---------------- #

@router.put("/go-online/{worker_id}")
def go_online(
    worker_id: int,
    db: Session = Depends(get_db)
):

    worker = db.query(Worker).filter(
        Worker.id == worker_id
    ).first()

    if not worker:
        return {
            "message": "Worker not found"
        }

    worker.is_online = True

    db.commit()

    return {
        "message": "Worker is now online"
    }


# ---------------- GO OFFLINE ---------------- #

@router.put("/go-offline/{worker_id}")
def go_offline(
    worker_id: int,
    db: Session = Depends(get_db)
):

    worker = db.query(Worker).filter(
        Worker.id == worker_id
    ).first()

    if not worker:
        return {
            "message": "Worker not found"
        }

    worker.is_online = False

    db.commit()

    return {
        "message": "Worker is now offline"
    }


# ---------------- NEARBY WORKERS ---------------- #

@router.get("/nearby")
def nearby_workers(
    db: Session = Depends(get_db)
):

    workers = db.query(Worker).filter(
        Worker.is_online == True
    ).all()

    return workers