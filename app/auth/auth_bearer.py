from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from app.auth.jwt_handler import verify_token

class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):

        credentials = await super().__call__(request)

        if credentials:

            token = credentials.credentials

            payload = verify_token(token)

            if payload is None:

                raise HTTPException(
                    status_code=403,
                    detail="Invalid token"
                )

            return payload

        raise HTTPException(
            status_code=403,
            detail="Invalid authorization"
        )