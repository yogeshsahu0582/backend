from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from app.database.connection import Base

class Booking(Base):

    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(Integer)

    worker_id = Column(
        Integer,
        nullable=True
    )

    service_type = Column(String)

    status = Column(
        String,
        default="pending"
    )

    amount = Column(
        Float,
        default=0
    )