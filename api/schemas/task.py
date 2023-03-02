from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="醤油を取りに行く")


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True