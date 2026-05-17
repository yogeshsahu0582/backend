from sqlalchemy import (
    Column,
    Integer,
    String
)

from app.database.connection import Base

class FCMToken(Base):

    __tablename__ = "fcm_tokens"

    id = Column(Integer, primary_key=True, index=True)

    user_type = Column(String)

    user_id = Column(Integer)

    fcm_token = Column(String)