from pydantic import BaseModel


class TodoListRequest(BaseModel):
    title: str
    description: str
    user_id: int


class TodoListResponse(TodoListRequest):
    id: int
