from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime
)

from datetime import datetime

from app.database.connection import Base


class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(Integer)

    total_amount = Column(Float)

    platform_commission = Column(Float)

    worker_earnings = Column(Float)

    payment_status = Column(
        String,
        default="pending"
    )

    payment_method = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )