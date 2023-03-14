from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from config.database import Session

from schemas.author_book import BookSchema

from services.book import BookService

book_router = APIRouter()


@book_router.get('/books', tags=['book'], response_model=List[BookSchema], response_model_exclude={'blurb'}, response_model_by_alias=True, status_code=200)
def get_books() -> List[BookSchema]:
    db = Session()
    result = BookService(db).getBooks()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@book_router.get('/book/{id}', tags=['book'], response_model=BookSchema, response_model_exclude={'blurb'}, response_model_by_alias=True, status_code=200)
def get_book(id: int = Path(ge=1)) -> BookSchema:
    db = Session()
    result = BookService(db).getBook(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Not Found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
