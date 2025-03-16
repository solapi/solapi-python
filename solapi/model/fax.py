from pydantic import BaseModel


class FileIdsType(BaseModel):
    file_ids: list[str]