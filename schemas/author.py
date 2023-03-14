from typing import List, Optional
from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    id: int = Field(alias='author_id')
    name: str = Field(alias='author_name')
    blurb: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
