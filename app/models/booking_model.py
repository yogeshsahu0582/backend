from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.connection import Base


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_phone = Column(
        String,
        nullable=False
    )

    worker_name = Column(
        String,
        nullable=True
    )

    service_type = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    duration = Column(
        String,
        nullable=False
    )

    location = Column(
        String,
        nullable=False
    )

    latitude = Column(
        Float,
        default=0.0
    )

    longitude = Column(
        Float,
        default=0.0
    )

    price = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="pending"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )