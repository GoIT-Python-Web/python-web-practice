from abc import ABC, abstractclassmethod
from typing import Any


class Car:
    def __init__(self):
        self.parts = {}

    def add(self, key: str, value: Any):
        self.parts[key] = value

    def show(self):
        print("Автомобіль складається з:")
        for name, part in self.parts.items():
            print(f"{name}: {part}")


class Builder(ABC):
    @abstractclassmethod
    def build_wheels(self):
        pass

    @abstractclassmethod
    def build_doors(self):
        pass

    @abstractclassmethod
    def build_engine(self):
        pass

    @abstractclassmethod
    def get_result(self) -> Car:
        pass


class GasCarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двері", "4")

    def build_engine(self):
        self.car.add("Двигун", "V8")

    def get_result(self) -> Car:
        return self.car


class ElectricCarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двері", "2")

    def build_engine(self):
        self.car.add("Двигун", "Електричний")

    def get_result(self) -> Car:
        return self.car


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct(self):
        self.builder.build_wheels()
        self.builder.build_doors()
        self.builder.build_engine()


if __name__ == "__main__":
    # Клієнтський код
    gas_builder = GasCarBuilder()
    director = Director(gas_builder)
    director.construct()
    gas_car = gas_builder.get_result()
    print("Бензиновий автомобіль:")
    gas_car.show()

    electric_builder = ElectricCarBuilder()
    director = Director(electric_builder)
    director.construct()
    electric_car = electric_builder.get_result()
    print("\nЕлектромобіль:")
    electric_car.show()
