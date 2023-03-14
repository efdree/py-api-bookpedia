from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from middlewares.error_handler import ErrorHandler

from config.database import engine, Base

from models.model import Book, Author, BookAuthor

from config.database import Session

from routers.author import author_router
from routers.book import book_router
app = FastAPI()
app.title = "Bookipedia API"
app.version = "0.0.1"

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(author_router)
app.include_router(book_router)

Base.metadata.create_all(bind=engine)


with Session(bind=engine) as session:
    book1 = Book(title="Austin Powers")
    book2 = Book(title="Castaway")

    author1 = Author(name="Mike Meyers")
    author2 = Author(name="Seth Green")
    author3 = Author(name="Tom Hanks")

    session.add_all([book1, book2, author1, author2, author3])
    session.commit()

    book_author1 = BookAuthor(
        book_id=book1.id, author_id=author1.id, blurb="Austin Powers")
    book_author2 = BookAuthor(
        book_id=book1.id, author_id=author1.id, blurb="Dr. Evil")
    book_author3 = BookAuthor(
        book_id=book1.id, author_id=author2.id, blurb="Scott")
    book_author4 = BookAuthor(
        book_id=book2.id, author_id=author3.id, blurb="Chuck")

    session.add_all([book_author1, book_author2, book_author3, book_author4])
    session.commit()
