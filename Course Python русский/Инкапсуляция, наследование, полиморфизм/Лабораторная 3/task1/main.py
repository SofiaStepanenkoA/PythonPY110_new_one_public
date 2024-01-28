class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("name должно иметь строковый тип")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("author должно иметь строковый тип")
        self._author = author
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
    @property
    def author(self):
        return self._author

    @property
    def name(self):
        return self._name


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__( name, author)
        if not isinstance(pages, int):
            raise TypeError("pages должно быть целым числом")
        if pages <= 0:
            raise ValueError("pages должно быть положительным числом")
        self.pages = pages
    def __str__(self):
        return super().__str__()
    def __repr__(self,pages: int):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r},pages = {pages!r})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__( name, author)
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError("duration должно быть дробным числом")
        if duration <= 0:
            raise ValueError("duration должно быть положительным числом")
        self.duration = duration
    def __str__(self):
        return super().__str__()
    def __repr__(self, duration: float):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r},duraction = {duration!r})"

if __name__ == '__main__':
    book1 = Book('World_and_peace','Tolstoy')
    print(book1.name)
    print(book1.author)
    audio_book = AudioBook('palata6','Chechov',11.5)
    print(audio_book.author)