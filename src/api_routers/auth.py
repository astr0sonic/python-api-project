from fastapi import APIRouter
from sqlalchemy import text

from src.database import engine
from src.models.user import UserRequest, UserResponse

auth = APIRouter(
    prefix="/auth",
    tags=["Registration/authorization"],
)


@auth.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION();"))
        print(res.one())

    return UserResponse(
        id=1,
        username=user.username,
    )


@auth.post("/sign-in")
async def sign_in(user: UserRequest) -> UserResponse:
    return UserResponse(
        id=1,
        username=user.username,
    )
