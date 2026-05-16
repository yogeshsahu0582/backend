from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.user_model import User

from app.models.worker_model import Worker

from app.schemas.auth_schema import LoginRequest

from app.auth.jwt_handler import create_access_token

from app.middleware.limiter import limiter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/user-login")
@limiter.limit("5/minute")
def user_login(
    request: Request,
    login_request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.phone == login_request.phone
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "role": "user"
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id
    }


@router.post("/worker-login")
@limiter.limit("5/minute")
def worker_login(
    request: Request,
    login_request: LoginRequest,
    db: Session = Depends(get_db)
):

    worker = db.query(Worker).filter(
        Worker.phone == login_request.phone
    ).first()

    if not worker:

        raise HTTPException(
            status_code=404,
            detail="Worker not found"
        )

    token = create_access_token(
        {
            "worker_id": worker.id,
            "role": "worker"
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "worker_id": worker.id
    }