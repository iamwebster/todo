from fastapi import APIRouter 

from app.schemas.todo_validation import TaskData
from app.database.mysql_connector import connector


router = APIRouter(prefix='/api/v1')


@router.get("/todo", tags=['todo'])
async def get_all_tasks():
    result = await connector.get_all_tasks()
    return result 


@router.post("/todo", tags=['todo'])
async def create_new_task(task_data: TaskData):
    result = await connector.create_new_task(task_data)
    return result


@router.get("/todo/{task_id}", tags=['todo'])
async def get_detail_task(task_id: int):
    result = await connector.get_detail_task(task_id)
    return result


@router.put("/todo/{task_id}", tags=['todo'])
async def update_task(task_id: int, task_data: TaskData):
    result = await connector.update_task(task_id, task_data)
    return result


@router.delete("/todo/{task_id}", tags=['todo'])
async def delete_task(task_id: int):
    result = await connector.delete_task(task_id)
    return result