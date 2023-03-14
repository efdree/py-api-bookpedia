from typing import List
from schemas.author import AuthorBase
from schemas.book import BookBase


class BookSchema(BookBase):
    authors: List[AuthorBase]


class AuthorSchema(AuthorBase):
    books: List[BookBase]
