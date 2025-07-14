from typing import Literal

from pydantic import BaseModel, ConfigDict


class Bms(BaseModel):
    targeting: Literal["M", "N", "I"]

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
    )
