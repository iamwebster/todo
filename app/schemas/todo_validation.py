from typing import Optional
from pydantic import BaseModel 


class TaskData(BaseModel):
    title: str
    text: Optional[str] = None
    