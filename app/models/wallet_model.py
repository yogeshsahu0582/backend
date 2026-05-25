from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.connection import Base


class Wallet(Base):

    __tablename__ = "wallets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    phone = Column(
        String,
        nullable=False
    )

    balance = Column(
        Float,
        default=0
    )

    role = Column(
        String,
        default="user"
    )