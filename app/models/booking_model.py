from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from datetime import datetime

from app.database.connection import Base

class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    worker_id = Column(
        Integer,
        ForeignKey("workers.id")
    )

    service_type = Column(String)

    status = Column(
        String,
        default="pending"
    )

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )