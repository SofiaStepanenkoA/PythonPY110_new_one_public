BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("ID должно быть целым числом")
        if id_ <= 0:
            raise ValueError("ID должно быть положительным числом")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError("name должно быть строкой")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("pages должно быть целым числом")
        if pages <= 0:
            raise ValueError("pages должно быть положительным числом")
        self.pages = pages

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name}, pages={self.pages})'

    def __str__(self):
        return f'Книга: {self.name!r}'


# TODO написать класс Library
class Library:
    def __init__(self, books: list=None):
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        max_ = 0
        for book in self.books:
            if max_<book.id_:
                max_ = book.id_
        return max_+1

    def get_index_by_book_id(self,id) -> int:
        for i, book in enumerate (self.books):
            if book.id_ == id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
