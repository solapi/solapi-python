from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, model_validator
from pydantic.alias_generators import to_camel


class VoiceOption(BaseModel):
    voice_type: Literal["FEMALE", "MALE"]
    header_message: Optional[str] = None
    tail_message: Optional[str] = None
    reply_range: Optional[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]] = None
    counselor_number: Optional[str] = None

    @model_validator(mode="after")
    def check_exclusive_fields(self) -> "VoiceOption":
        if self.reply_range is not None and self.counselor_number is not None:
            raise ValueError(
                "reply_range와 counselor_number는 같이 사용할 수 없습니다."
            )
        return self

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="ignore",
    )
