from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.models.user_model import User
from app.models.worker_model import Worker
from app.models.booking_model import Booking
from app.models.payment_model import Payment
from app.models.sos_model import SOSAlert

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def admin_dashboard(
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_workers = db.query(Worker).count()

    online_workers = db.query(
        Worker
    ).filter(
        Worker.is_online == True
    ).count()

    active_bookings = db.query(
        Booking
    ).filter(
        Booking.status.in_(
            ["accepted", "in_progress"]
        )
    ).count()

    total_revenue = 0

    payments = db.query(Payment).all()

    for payment in payments:

        total_revenue += payment.platform_commission

    active_sos = db.query(
        SOSAlert
    ).filter(
        SOSAlert.status == "active"
    ).count()

    return {
        "total_users": total_users,
        "total_workers": total_workers,
        "online_workers": online_workers,
        "active_bookings": active_bookings,
        "platform_revenue": total_revenue,
        "active_sos_alerts": active_sos
    }