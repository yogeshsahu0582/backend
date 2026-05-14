from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.connection import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    worker_id = Column(Integer, ForeignKey("workers.id"))

    service_type = Column(String)

    status = Column(String, default="pending")