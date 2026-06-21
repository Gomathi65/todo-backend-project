from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True