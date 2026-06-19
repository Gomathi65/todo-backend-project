from pydantic import BaseModel, Field
from typing import Optional


# CREATE TODO (input from user)
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)


# UPDATE TODO (partial update)
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=200)
    completed: Optional[bool] = None


# RESPONSE (what API sends back)
class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True