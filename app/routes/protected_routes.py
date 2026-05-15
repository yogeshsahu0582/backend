from fastapi import APIRouter, Depends

from app.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)

@router.get("/profile")
def protected_profile(
    payload=Depends(JWTBearer())
):

    return {
        "message": "Protected Route Accessed",
        "payload": payload
    }