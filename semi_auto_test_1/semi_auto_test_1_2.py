"""Полуавтоматическое тестирование для функции full_name(semi_auto_test_1_1.py)."""
from semi_auto_test_1_1 import full_name

print("Для остановки теста нажмите 'Q'")
while True:
    name = input("\nВведите ваше имя: ")
    if name == "Q":
        print("Выход")
        break
    last_name = input("\nВведите вашу фамилию: ")
    if last_name == "Q":
        print("Выход")
        break

    format_name = full_name(name, last_name)
    print("\tФорматирование имени: " + format_name)
