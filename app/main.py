from fastapi import FastAPI

from app.api import todo_endpoints

app = FastAPI()
app.include_router(todo_endpoints.router)
