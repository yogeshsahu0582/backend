from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database.connection import Base


class Rating(Base):

    __tablename__ = "ratings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    booking_id = Column(
        Integer,
        nullable=False
    )

    worker_name = Column(
        String,
        nullable=False
    )

    review = Column(
        String,
        nullable=True
    )

    stars = Column(
        Float,
        default=5
    )