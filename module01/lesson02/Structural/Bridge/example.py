from abc import ABC, abstractmethod
from enum import Enum


class TypeShape(str, Enum):
    circle = "circle"
    square = "square"


# Implementor
class DrawingAPI(ABC):
    @abstractmethod
    def draw_shape(self, x, y, shape):
        pass


# ConcreteImplementor
class DrawingAPIGreen(DrawingAPI):
    def draw_shape(self, x, y, shape):
        print(f"Green drawing a {shape} at {x}:{y}")


# ConcreteImplementor
class DrawingAPIBlue(DrawingAPI):
    def draw_shape(self, x, y, shape):
        print(f"Blue drawing a {shape} at {x}:{y}")


# Abstraction
class Shape(ABC):
    def __init__(self, x, y, drawing_api: DrawingAPI):
        self.x = x
        self.y = y
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass


# RefinedAbstraction
class CircleShape(Shape):
    def draw(self):
        self.drawing_api.draw_shape(self.x, self.y, TypeShape.circle)


# RefinedAbstraction
class SquareShape(Shape):
    def draw(self):
        self.drawing_api.draw_shape(self.x, self.y, TypeShape.square)


if __name__ == "__main__":
    # Клієнтський код
    shapes = [
        CircleShape(1, 2, DrawingAPIGreen()),
        SquareShape(5, 7, DrawingAPIBlue()),
    ]

    for shape in shapes:
        shape.draw()
