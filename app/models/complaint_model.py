from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.connection import Base

class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(Integer)

    raised_by = Column(String)

    complaint_message = Column(String)

    status = Column(
        String,
        default="open"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )