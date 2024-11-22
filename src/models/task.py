from pydantic import BaseModel


class TaskRequest(BaseModel):
    title: str
    description: str
    done: bool
    list_id: int


class TaskResponse(TaskRequest):
    id: int
