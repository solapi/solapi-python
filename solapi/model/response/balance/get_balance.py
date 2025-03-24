from typing import Optional

from pydantic import BaseModel


class GetBalanceResponse(BaseModel):
    balance: Optional[float] = None
    point: Optional[float] = None
