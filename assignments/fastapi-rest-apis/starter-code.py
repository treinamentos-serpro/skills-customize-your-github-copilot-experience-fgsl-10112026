from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookInput(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", year=1962),
}


@app.get("/books", response_model=list[Book])
def list_books(author: str | None = None) -> list[Book]:
    # TODO: Return all books; later, filter by the optional author parameter.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Return the requested book or raise HTTPException with status 404.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput) -> Book:
    # TODO: Create a book with a new ID, store it, and return it.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Replace the requested book or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Delete the requested book or raise HTTPException with status 404.
    raise NotImplementedError
