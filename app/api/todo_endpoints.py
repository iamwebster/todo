from fastapi import APIRouter 


router = APIRouter(prefix='/api/v1')


@router.get("/todo")
async def get_all_tasks():
    pass 


@router.post("/todo")
async def create_new_task():
    pass 


@router.get("/todo/{task_id}")
async def get_detail_task(task_id: int):
    pass 


@router.put("/todo/{task_id}")
async def update_task(task_id: int):
    pass 


@router.delete("/todo/{task_id}")
async def delete_task(task_id: int):
    pass 