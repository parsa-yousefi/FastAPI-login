from typing import Optional

from pydantic import BaseModel


class CreateRequest(BaseModel):
    username: str
    password: str
    isAdmin: Optional[bool] = False

