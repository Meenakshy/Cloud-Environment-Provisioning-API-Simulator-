from pydantic import BaseModel # type: ignore
from datetime import datetime

class EnvironmentCreate(BaseModel):
    name: str
    owner: str
    region: str
    size: str

class EnvironmentRead(EnvironmentCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
