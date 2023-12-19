"""
Sequence - це більш специфічний тип, ніж Iterable. Він належить до стандартних контейнерних протоколів у Python і представляє колекції, які підтримують індексацію та ітерацію. Іншими словами, крім здатності ітеруватися (як Iterable), Sequence також підтримує отримання елементів за конкретним індексом.
"""

from typing import Sequence


def first_element(items: Sequence[int]) -> int:
    return items[3]


numbers = [1, 2, 3, 4, 5]
print(first_element(numbers))  # Виведе: 1
