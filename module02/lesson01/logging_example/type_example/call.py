"""
В модулі typing, Callable використовується для опису змінних або об'єктів, які "викликаються", тобто можуть бути використані як функції. Це корисно, коли ви хочете передати функцію як аргумент іншій функції, або коли ви хочете повернути функцію з функції.
"""

#  Callable[[Arg1Type, Arg2Type, ...], ReturnType]

from typing import Callable, Any


def call_function(func: Callable[[], int]) -> int:
    return func()


def return_five() -> int:
    return 5


print(call_function(return_five))  # Виведе: 5


def call_function1(func: Callable[[int, int], str], x: int, y: int) -> str:
    return func(x, y)


def concatenate_numbers(a: int, b: int) -> str:
    return str(a) + str(b)


print(call_function1(concatenate_numbers, 2, 3))  # Виведе: '23'


def call_function2(func: Callable[..., str], *args: Any) -> str:
    return func(*args)


print(call_function2(str, 12345))  # Виведе: '12345'
