from enum import Enum
from abc import ABC, abstractmethod

# Abstract Factory


class OperationType(str, Enum):
    SUM = "summation operation"
    MUL = "multiplication operation"


class Operation(ABC):
    def __init__(self):
        self.data = None

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Adder(Operation):
    def __init__(self, data: list[int]):
        super().__init__()
        self.data = data

    def operation(self):
        return sum(self.data)

    def info(self):
        return OperationType.SUM


class Multiplier(Operation):
    def __init__(self, data: list[int]):
        super().__init__()
        self.data = data

    def operation(self):
        mul = 1
        for el in self.data:
            mul *= el
        return mul

    def info(self):
        return OperationType.MUL


class Factory(ABC):
    @abstractmethod
    def create_operation(self) -> Operation:
        pass

    def make_operation(self) -> Operation:
        operation = self.create_operation()
        return operation


class SumFactory(Factory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Adder(self.data)


class MulFactory(Factory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Multiplier(self.data)


def calculation(factory: Factory):
    operator: Operation = factory.make_operation()
    result = operator.operation()
    return result, operator.info(), operator.data


if __name__ == "__main__":
    data = [29, 30, 1, 2, 3, 4, 5]
    result, type_operation, data = calculation(SumFactory(data))
    print(f"Результат: {result}, Тип операції: {type_operation}, Дані: {data}")
    print(calculation(MulFactory(data)))
    print(f"{OperationType.MUL}")
