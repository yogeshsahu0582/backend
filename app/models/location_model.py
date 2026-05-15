from sqlalchemy import Column, Integer, Float, ForeignKey

from app.database.connection import Base

class Location(Base):

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)

    worker_id = Column(
        Integer,
        ForeignKey("workers.id")
    )

    latitude = Column(Float)

    longitude = Column(Float)