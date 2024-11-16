from fastapi import APIRouter

lists = APIRouter(prefix="/lists")


@lists.get("")
async def get_lists() -> str:
    return "lists"


@lists.get("/{list_id}")
async def get_list(list_id: int):
    return f"list: {list_id}"


@lists.post("")
async def create_list() -> str:
    return "list"


@lists.put("/{list_id}")
async def update_list(list_id: int) -> str:
    return f"list: {list_id}"


@lists.delete("/{list_id}")
async def delete_list(list_id: int) -> str:
    return f"list: {list_id}"


@lists.post("/{list_id}/tasks")
async def create_task(list_id: int) -> str:
    return f"new task was created in list {list_id}"


@lists.get("/{list_id}/tasks")
async def get_tasks(list_id: int) -> str:
    return f"tasks of list: {list_id}"
