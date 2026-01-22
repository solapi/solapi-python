from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

KAKAO_TV_URL_PREFIX = "https://tv.kakao.com/"


class BmsVideo(BaseModel):
    video_url: str
    image_id: Optional[str] = None
    image_link: Optional[str] = None

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    @field_validator("video_url")
    @classmethod
    def validate_kakao_tv_url(cls, v: str) -> str:
        if not v.startswith(KAKAO_TV_URL_PREFIX):
            raise ValueError(
                f"videoUrl은 '{KAKAO_TV_URL_PREFIX}'으로 시작하는 "
                "카카오TV 동영상 링크여야 합니다."
            )
        return v
