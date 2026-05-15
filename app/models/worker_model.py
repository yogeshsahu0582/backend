from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float
)

from app.database.connection import Base

class Worker(Base):

    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    phone = Column(
        String,
        unique=True,
        nullable=False
    )

    skill_type = Column(String)

    is_online = Column(
        Boolean,
        default=False
    )

    is_busy = Column(
        Boolean,
        default=False
    )

    rating = Column(
        Float,
        default=5.0
    )

    is_verified = Column(
        Boolean,
        default=False
    )