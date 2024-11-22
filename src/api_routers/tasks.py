from fastapi import APIRouter

from models.task import TaskRequest, TaskResponse

tasks = APIRouter(
    prefix="/tasks",
    tags=["Tasks processing"],
)


@tasks.get("/{task_id}")
async def get_task(task_id: int) -> TaskResponse:
    return TaskResponse(
        id=task_id,
        title="Task 1",
        description="My task",
        done=False,
        list_id=1,
    )


@tasks.put("/{task_id}")
async def update_task(task_id: int, task: TaskRequest) -> TaskResponse:
    return TaskResponse(
        id=task_id,
        title=task.title,
        description=task.description,
        done=task.done,
        list_id=1,
    )


@tasks.delete("/{task_id}")
async def delete_task(task_id: int) -> TaskResponse:
    return TaskResponse(
        id=task_id,
        title="Task 1",
        description="My task",
        done=False,
        list_id=1,
    )
