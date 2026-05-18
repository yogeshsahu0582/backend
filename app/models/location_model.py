from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime
)

from datetime import datetime

from app.database.connection import Base

class Location(Base):

    __tablename__ = "locations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    worker_id = Column(
        Integer,
        unique=True
    )

    latitude = Column(Float)

    longitude = Column(Float)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow
    )