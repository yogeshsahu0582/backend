from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.payment_model import Payment

from app.schemas.payment_schema import PaymentCreate

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

PLATFORM_COMMISSION_PERCENT = 7


@router.post("/create")
def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db)
):

    commission = (
        payment.total_amount *
        PLATFORM_COMMISSION_PERCENT
    ) / 100

    worker_earnings = (
        payment.total_amount -
        commission
    )

    new_payment = Payment(
        booking_id=payment.booking_id,
        total_amount=payment.total_amount,
        platform_commission=commission,
        worker_earnings=worker_earnings,
        payment_status="completed",
        payment_method=payment.payment_method
    )

    db.add(new_payment)

    db.commit()

    db.refresh(new_payment)

    return {
        "message": "Payment completed",
        "payment_id": new_payment.id,
        "platform_commission": commission,
        "worker_earnings": worker_earnings
    }


@router.get("/worker-earnings/{worker_id}")
def worker_earnings(
    worker_id: int,
    db: Session = Depends(get_db)
):

    payments = db.query(Payment).all()

    total_earnings = 0

    for payment in payments:

        total_earnings += payment.worker_earnings

    return {
        "worker_id": worker_id,
        "total_earnings": total_earnings
    }


@router.get("/admin/revenue")
def admin_revenue(
    db: Session = Depends(get_db)
):

    payments = db.query(Payment).all()

    total_revenue = 0

    total_worker_payout = 0

    total_transactions = 0

    for payment in payments:

        total_revenue += payment.platform_commission

        total_worker_payout += payment.worker_earnings

        total_transactions += payment.total_amount

    return {
        "platform_revenue": total_revenue,
        "worker_payouts": total_worker_payout,
        "total_transactions": total_transactions
    }


@router.get("/history")
def payment_history(
    db: Session = Depends(get_db)
):

    payments = db.query(Payment).all()

    return payments