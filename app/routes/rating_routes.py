from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.rating_model import Rating

router = APIRouter(
    prefix="/rating",
    tags=["Ratings"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/add")

def add_rating(

    booking_id: int,

    worker_name: str,

    review: str,

    stars: float,

    db: Session = Depends(get_db)
):

    rating = Rating(

        booking_id=booking_id,

        worker_name=worker_name,

        review=review,

        stars=stars
    )

    db.add(rating)

    db.commit()

    return {
        "message":
            "Rating added"
    }


@router.get("/{worker_name}")

def get_worker_ratings(

    worker_name: str,

    db: Session = Depends(get_db)
):

    ratings = db.query(
        Rating
    ).filter(
        Rating.worker_name == worker_name
    ).all()

    return ratings