import doctest
class Passenger:
    def __int__(self, name:str, age:int):
        """
               Создание и подготовка к работе объекта "Passenger"

               :name: Имя пассажира
               :age: Возраст пассажира

               Примеры:
               >>> Pass1 = Passenger('Джон', 50)  # инициализация экземпляра класса
               """
        if not isinstance(name, str):
            raise TypeError("Имя пассажира должно иметь строковый тип")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст пассажира должен быть целым числом")
        if age <= 0:
            raise ValueError("Возраст пассажира должен быть положительным числом")
        self.age = age
    def flight_num(self) -> int:
        """
                Функция которая возвращает количество полетов

                :return: возвращает количество полетов

                Примеры:
                >>> Pass1 = Passenger('Джон', 50)
                >>> Pass1.flight_num()
                """
        ...
    def customer_discount(self) -> int:
        """
                Функция которая возвращает процент скидки пассажира

                :return: возвращает процент скидки пассажира

                Примеры:
                >>> Pass1 = Passenger('Джон', 50)
                >>> Pass1.customer_discount()
                """
        ...
class Plane:
    def __int__(self, bort_num:int, length:float, width:float):
        """
                       Создание и подготовка к работе объекта "Plane"

                       :bort_num: Номер борта
                       :length: Длина судна
                       :width: Ширина судна

                       Примеры:
                       >>> Plane1 = Plane(123, 100.2, 56.7)  # инициализация экземпляра класса
                       """
        if not isinstance(bort_num, int):
            raise TypeError("Номер борта должен быть целым числом")
        if bort_num <= 0:
            raise ValueError("Номер борта должен быть положительным числом")
        self.bort_num = bort_num

        if not isinstance(length, float):
            raise TypeError("Длина судна должна быть дробным числом")
        if length <= 0:
            raise ValueError("Длина судна должна быть положительным числом")
        self.length = length

        if not isinstance(width, float):
            raise TypeError("Ширина судна должна быть дробным числом")
        if width <= 0:
            raise ValueError("Ширина судна должна быть положительным числом")
        self.width = width
    def calcuilate_weight(self) -> float:
        """
                    Функция которая возвращает вес судна

                    :return: возвращает вес судна

                    Примеры:
                    >>> Plane1 = Plane(123, 100.2, 56.7)
                    >>> Plane1.calcuilate_weight()
                    """
        ...
    def get_model(self) -> str:
        """
                    Функция которая возвращает модель судна

                    :return: возвращает модель судна

                    Примеры:
                    >>> Plane1 = Plane(123, 100.2, 56.7)
                    >>> Plane1.get_model()
                    """
        ...
    def get_time_flight(self) -> int:
        """
                    Функция которая возвращает время вылета

                    :return: возвращает время вылета

                    Примеры:
                    >>> Plane1 = Plane(123, 100.2, 56.7)
                    >>> Plane1.get_time_flight()
                    """
        ...

class Crew:
    def __int__(self, captain_name:str, crew_number:int, average_age:float):
        """
                        Создание и подготовка к работе объекта "Crew"

                        :captain_name: Имя командира
                        :crew_number: Количество экипажа
                        :average_age: Средний возраст

                        Примеры:
                        >>> Crew1 = Crew("Ivan", 8, 28)  # инициализация экземпляра класса
                        """
        if not isinstance(captain_name, str):
            raise TypeError("Имя командира должно иметь строковый тип")
        self.captain_name = captain_name
        if not isinstance(crew_number, int):
            raise TypeError("Количество экипажа должно быть целым числом")
        if crew_number <= 0:
            raise ValueError("Количество экипажа должно быть положительным числом")
        self.crew_number = crew_number

        if not isinstance(average_age, float):
            raise TypeError("Средний возраст должен быть дробным числом")
        if average_age <= 0:
            raise ValueError("Средний возраст должен быть положительным числом")
        self.average_age = average_age
    def get_experience(self) -> float:
        """
                    Функция которая возвращает опыт экипажа по десятибальной шкале

                    :return: возвращает дробное число - опыт экипажа

                    Примеры:
                    >>> Crew1 = Crew("Ivan", 8, 28)
                    >>> Crew1.get_experience()
                    """
        ...
    def get_rate(self) -> float:
        """
                    Функция, которая возвращает оценку экипажа пассажирами

                    :return: возвращает дробное число - оценку экипажа пассажирами

                    Примеры:
                    >>> Crew1 = Crew("Ivan", 8, 28)
                    >>> Crew1.get_rate()
                    """
        ...


# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
