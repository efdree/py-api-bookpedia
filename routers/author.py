from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from config.database import Session

from schemas.author_book import AuthorSchema

from services.author import AuthorService

author_router = APIRouter()


@author_router.get('/authors', tags=['author'], response_model=List[AuthorSchema], response_model_exclude={'blurb'}, response_model_by_alias=True, status_code=200)
def get_authors() -> List[AuthorSchema]:
    db = Session()
    result = AuthorService(db).getAuthors()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@author_router.get('/author/{id}', tags=['author'], response_model=AuthorSchema, response_model_exclude={'blurb'}, response_model_by_alias=True, status_code=200)
def get_author(id: int = Path(ge=1)) -> AuthorSchema:
    db = Session()
    result = AuthorService(db).getAuthor(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
