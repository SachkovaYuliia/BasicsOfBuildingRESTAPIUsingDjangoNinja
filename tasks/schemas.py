from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str
    status: str
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    due_date: Optional[datetime]
    created_at: datetime

    class Config:
         from_attributes = True