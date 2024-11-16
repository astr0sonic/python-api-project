from fastapi import APIRouter

tasks = APIRouter(prefix="/tasks")


@tasks.get("/{task_id}")
async def get_task(task_id: int) -> str:
    return f"task: {task_id}"


@tasks.put("/{task_id}")
async def update_task(task_id: int) -> str:
    return f"task: {task_id}"


@tasks.delete("/{task_id}")
async def delete_task(task_id: int) -> str:
    return f"task: {task_id}"
