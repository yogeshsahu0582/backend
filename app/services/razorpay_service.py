import razorpay

from app.config.settings import (
    RAZORPAY_KEY_ID,
    RAZORPAY_KEY_SECRET
)

client = razorpay.Client(
    auth=(
        RAZORPAY_KEY_ID,
        RAZORPAY_KEY_SECRET
    )
)

def create_razorpay_order(
    amount: int
):

    order = client.order.create(
        {
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1
        }
    )

    return order