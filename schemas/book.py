from typing import List, Optional
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    id: int = Field(alias='book_id')
    title: str = Field(alias='book_title')
    blurb: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
