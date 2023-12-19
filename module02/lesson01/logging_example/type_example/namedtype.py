from typing import NamedTuple


# Описуємо структуру для представлення особи
class Person(NamedTuple):
    name: str
    age: int
    height: float


# Створюємо екземпляр
john = Person(name="John", age=30, height=180.5)

# Доступ до полів
print(john.name)  # John
print(john.age)  # 30
print(john.height)  # 180.5
