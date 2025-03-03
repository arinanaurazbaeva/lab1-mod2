# TODO Написать 3 класса с документацией и аннотацией типов
import time

class Person:
    def __init__(self, name, age, gender, wallet):
        """
        Поле name содержит имя данного человека, поле age содержит информацию о возрасте данного
        человека, поле gender содержит пол данного человека, поле wallet содержит
        информацию о количестве в кошельке данного человека.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.wallet = wallet

    def talk(self, phrase):
        """
        Функция talk() предназначена для реализации высказываний объекта класса Person,
        в качестве параметра передается аргумент типа str. Реализация функционала
        заключается в выводе передаваемой фразы в консоль.
        Пример:
            person.talk("Hello!")
            Вывод:
                Hello!
        """
        print(phrase)

    def give_money(self, recipient, cnt_money):
        recipient.talk(recipient.name + ": " + self.name + ", дай мне " +
                       str(cnt_money))
        if self.wallet >= cnt_money:
            self.wallet -= cnt_money
            recipient.wallet += cnt_money
            recipient.talk(recipient.name + ": Спасибо, " + self.name)
        else:
            recipient.talk(self.name + ": У меня столько нет " + recipient.name)

class Дерево:
    """Класс описывает дерево."""

    def __init__(self, вид: str, возраст: int, высота: float):
        """ Инициализация дерева. :param вид: Вид дерева (например, "Дуб", "Береза"). :param возраст: Возраст дерева в годах. :param высота: Высота дерева в метрах. :raises ValueError: Если возраст или высота отрицательные. """
        if возраст < 0 or высота < 0:
            raise ValueError("Возраст и высота дерева должны быть неотрицательными числами.")
        self.вид = вид
        self.возраст = возраст
        self.высота = высота

    def вырасти(self, прирост: float) -> None:
        """ Увеличивает высоту дерева на указанный прирост. :param прирост: Прирост высоты в метрах. :raises ValueError: Если прирост отрицательный. """
        if прирост < 0:
            raise ValueError("Прирост высоты должен быть положительным числом.")
        self.высота += прирост

    def стареть(self, годы: int) -> None:
        """ Увеличивает возраст дерева на указанное количество лет. :param годы: Количество лет, на которое увеличивается возраст. :raises ValueError: Если количество лет отрицательное. """
        if годы < 0:
            raise ValueError("Количество лет должно быть положительным числом.")
        self.возраст += годы

class Facebook:
    """Класс описывает социальную сеть Facebook."""
    def __init__(self, имя_пользователя: str, пароль: str):
        """ Инициализация аккаунта Facebook. :param имя_пользователя: Имя пользователя. :param пароль: Пароль пользователя. :raises ValueError: Если имя пользователя или пароль пустые строки. """
        if not имя_пользователя or not пароль:
            raise ValueError("Имя пользователя и пароль не могут быть пустыми строками.")
        self.имя_пользователя = имя_пользователя
        self.__пароль = пароль

    def опубликовать_пост(self, текст: str) -> bool:
        """ Публикует пост на стене пользователя. :param текст: Текст поста. :return: True, если публикация успешна; False, если произошла ошибка. """
        return True

    def отправить_сообщение(self, получатель: str, сообщение: str) -> bool:
        """ Отправляет личное сообщение другому пользователю. :param получатель: Имя пользователя-получателя. :param сообщение: Текст сообщения. :return: True, если отправка успешна; False, если произошла ошибка. """
        return True

if __name__ == "__main__":
    arina = Person("Арина", 21, "женский", 100)
    artur = Person("Артур", 20, "мужской", 30000)
    milena = Person("Милена", 20, "женский", 0)

    arina.talk("Привет, Артур, я вернулась")
    time.sleep(2)

    artur.talk("Привет,Арина, я тебя люблю")

    artur.give_money(arina, 2000)
    time.sleep(2)
    artur.give_money(milena, 100000)
