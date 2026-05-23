from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/user-login")
def user_login(data: dict):

    phone = data.get("phone")

    return {
        "access_token":
            "demo_token",

        "phone":
            phone
    }


@router.post("/worker-login")
def worker_login(data: dict):

    phone = data.get("phone")

    return {
        "access_token":
            "worker_demo_token",

        "phone":
            phone
    }