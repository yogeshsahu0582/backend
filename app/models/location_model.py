from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.connection import Base


class Location(Base):

    __tablename__ = "locations"

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

    latitude = Column(
        Float,
        default=0
    )

    longitude = Column(
        Float,
        default=0
    )

    status = Column(
        String,
        default="moving"
    )