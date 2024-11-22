from typing import List

from fastapi import APIRouter

from models.task import TaskRequest, TaskResponse
from models.todo_list import TodoListRequest, TodoListResponse

lists = APIRouter(
    prefix="/lists",
    tags=["Todo lists processing"],
)


@lists.get("")
async def get_lists() -> List[TodoListResponse]:
    return [
        TodoListResponse(
            id=1,
            title="My list 1",
            description="My description",
            user_id=1,
        ),
        TodoListResponse(
            id=2,
            title="My list 2",
            description="My description",
            user_id=1,
        ),
    ]


@lists.get("/{list_id}")
async def get_list(list_id: int) -> TodoListResponse:
    return TodoListResponse(
        id=list_id,
        title=f"My list {list_id}",
        description="My description",
        user_id=1,
    )


@lists.post("")
async def create_list(todo_list: TodoListRequest) -> TodoListResponse:
    return TodoListResponse(
        id=1,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.put("/{list_id}")
async def update_list(list_id: int, todo_list: TodoListRequest) -> str:
    return TodoListResponse(
        id=list_id,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.delete("/{list_id}")
async def delete_list(list_id: int) -> TodoListResponse:
    return TodoListResponse(
        id=list_id,
        title=f"My list {list_id}",
        description="My description",
        user_id=1,
    )


@lists.post("/{list_id}/tasks")
async def create_task(list_id: int, task: TaskRequest) -> TaskResponse:
    return TaskResponse(
        id=1,
        title=task.title,
        description=task.title,
        done=task.done,
        list_id=list_id,
    )


@lists.get("/{list_id}/tasks")
async def get_tasks(list_id: int) -> List[TaskResponse]:
    return [
        TaskResponse(
            id=1,
            title="Task 1",
            description="My task",
            done=False,
            list_id=list_id,
        ),
        TaskResponse(
            id=2,
            title="Task 2",
            description="My task",
            done=False,
            list_id=list_id,
        ),
    ]
