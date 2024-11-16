from fastapi import APIRouter

auth = APIRouter(prefix="/auth")


@auth.post("/sign-up")
async def sign_up() -> str:
    return "sign up"


@auth.post("/sign-in")
async def sign_in() -> str:
    return "sign in"
