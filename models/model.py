from config.database import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


class BookAuthor(Base):
    __tablename__ = 'book_authors'
    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books.id'))
    author_id = Column(ForeignKey('authors.id'))
    blurb = Column(String, nullable=False)

    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship(
        "BookAuthor", back_populates="book")


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("BookAuthor",
                         back_populates="author")
