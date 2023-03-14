from models.model import Author as AuthorModel
from models.model import BookAuthor as BookAuthorModel
from sqlalchemy.orm import joinedload


class AuthorService():

    def __init__(self, db) -> None:
        self.db = db

    def getAuthors(self):
        result = self.db.query(AuthorModel).options(
            joinedload(AuthorModel.books).options(
                joinedload(BookAuthorModel.book))).all()

        return result

    def getAuthor(self, id):
        result = self.db.query(AuthorModel).options(
            joinedload(AuthorModel.books).options(
                joinedload(BookAuthorModel.book))).where(AuthorModel.id == id).first()

        return result
