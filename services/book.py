from models.model import Book as BookModel
from models.model import BookAuthor as BookAuthorModel
from sqlalchemy.orm import joinedload


class BookService():

    def __init__(self, db) -> None:
        self.db = db

    def getBooks(self):
        result = self.db.query(BookModel).options(
            joinedload(BookModel.authors).options(
                joinedload(BookAuthorModel.author))).all()
        return result

    def getBook(self, id):
        result = self.db.query(BookModel).options(
            joinedload(BookModel.authors).options(
                joinedload(BookAuthorModel.author))).where(BookModel.id == id).first()
        return result
