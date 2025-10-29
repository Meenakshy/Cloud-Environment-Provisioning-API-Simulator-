from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional

class Environment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    owner: str
    region: str
    size: str
    status: str = Field(default="provisioning")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    