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
        return f'{self.__class__.__name__}(id_={self.id_}, name=\'{self.name}\', pages={self.pages})'

    def __str__(self):
        return f'Книга "{self.name}"'
if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
