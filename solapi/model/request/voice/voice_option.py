from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class VoiceOption(BaseModel):
    voice_type: Literal["FEMALE", "MALE"]
    header_message: Optional[str] = None
    tail_message: Optional[str] = None
    reply_range: Optional[int] = None
    counselor_number: Optional[str] = None

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )
