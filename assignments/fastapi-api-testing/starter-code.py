import pytest
from fastapi.testclient import TestClient

from main import app, books


client = TestClient(app)
initial_books = books.copy()


@pytest.fixture(autouse=True)
def reset_books():
    books.clear()
    books.update(initial_books)
    yield
    books.clear()
    books.update(initial_books)


def test_list_books_returns_all_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()) == len(initial_books)
    # TODO: Assert that each returned item includes the expected book fields.


def test_get_book_returns_requested_book():
    response = client.get("/books/1")

    assert response.status_code == 200
    # TODO: Assert that the response contains the expected ID and title.


# TODO: Add tests for missing IDs and the POST, PUT, and DELETE endpoints.
# TODO: Add tests for author filtering, including a case-insensitive match.
