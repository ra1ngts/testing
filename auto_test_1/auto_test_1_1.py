"""Функция для проверки через автоматическое тестирование."""


def full_name(last_name, name, patronymic=""):
    if patronymic:
        fully = last_name + " " + name + " " + patronymic
    else:
        fully = last_name + " " + name
    return fully.title()
