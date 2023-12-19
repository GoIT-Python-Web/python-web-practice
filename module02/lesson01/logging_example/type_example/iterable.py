"""
Iterable є однією з центральних концепцій в Python. У контексті типізації, Iterable - це тип, що вказує на те, що об'єкт може бути проходжений (ітерованим). Якщо клас реалізує метод __iter__(), він є ітерованим.

Основні характеристики:
Прохідність: Ви можете "проходитися" по Iterable об'єкту за допомогою циклу for.
Відсутність індексації: Не всі ітеровані об'єкти підтримують доступ до елементів за індексом (наприклад, множини).
"""

from typing import Iterable


def total_length(items: Iterable[str]) -> int:
    return sum(len(item) for item in items)


names = ["Alice", "Bob", "Charlie"]
result = total_length(names)
print(result)  # Виведе: 15
