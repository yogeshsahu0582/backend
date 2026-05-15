from pydantic import BaseModel

class PaymentCreate(BaseModel):

    booking_id: int

    total_amount: float

    payment_method: str