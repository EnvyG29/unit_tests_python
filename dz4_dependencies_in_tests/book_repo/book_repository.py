from abc import ABC, abstractmethod
from dz4_dependencies_in_tests.book_repo.book import Book


class BookRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> Book:
        pass

    @abstractmethod
    def find_all(self) -> list[Book]:
        pass
