from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import SessionLocal

from app.models.wallet_model import Wallet

router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/create")

def create_wallet(

    phone: str,

    role: str,

    db: Session = Depends(get_db)
):

    wallet = Wallet(

        phone=phone,

        role=role,

        balance=0
    )

    db.add(wallet)

    db.commit()

    return {
        "message":
            "Wallet created"
    }


@router.get("/{phone}")

def get_wallet(

    phone: str,

    db: Session = Depends(get_db)
):

    wallet = db.query(
        Wallet
    ).filter(
        Wallet.phone == phone
    ).first()

    if not wallet:

        return {
            "balance": 0
        }

    return {
        "balance":
            wallet.balance
    }


@router.post("/add-money")

def add_money(

    phone: str,

    amount: float,

    db: Session = Depends(get_db)
):

    wallet = db.query(
        Wallet
    ).filter(
        Wallet.phone == phone
    ).first()

    if wallet:

        wallet.balance += amount

        db.commit()

    return {
        "message":
            "Money added"
    }