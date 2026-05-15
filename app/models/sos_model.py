from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database.connection import Base

class SOSAlert(Base):

    __tablename__ = "sos_alerts"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(Integer)

    triggered_by = Column(String)

    message = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )