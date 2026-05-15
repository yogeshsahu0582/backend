from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean
)

from datetime import datetime

from app.database.connection import Base

class SOSAlert(Base):

    __tablename__ = "sos_alerts"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(Integer)

    triggered_by = Column(String)

    message = Column(String)

    emergency_level = Column(
        String,
        default="high"
    )

    admin_notified = Column(
        Boolean,
        default=False
    )

    contacts_notified = Column(
        Boolean,
        default=False
    )

    police_alert_requested = Column(
        Boolean,
        default=False
    )

    status = Column(
        String,
        default="active"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )