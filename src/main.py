import uvicorn
from fastapi import FastAPI

from src.api_routers.auth import auth
from src.api_routers.lists import lists
from src.api_routers.tasks import tasks

app = FastAPI()


@app.get("/hello")
async def print_hello() -> str:
    return "Hello, World!!!"


app.include_router(auth)
app.include_router(lists)
app.include_router(tasks)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
