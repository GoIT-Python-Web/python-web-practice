# lesson 01

S - Принцип единственной ответственности (Single responsibility)

O - Принцип открытости-закрытости (Open-closed)

> есть дополнительный пример storage_service.py

L - Принцип подстановки Барбары Лисков (Liskov substitution)

> есть дополнительные примеры про наследование

I - Принцип разделения интерфейса (Interface segregation)

D - Принцип инверсии зависимостей (Dependency inversion)


S.O.L.I.D — це акронім, який представляє п'ять ключових принципів об'єктно-орієнтованого програмування і проектування. Ці принципи допомагають розробникам створювати системи, які є масштабованими, розширюваними і легкими для підтримки.

## 1. S — Single Responsibility Principle (SRP)

### Опис:

Кожний клас повинен мати лише одну причину для зміни. Це означає, що кожен клас має нести відповідальність лише за одне конкретне завдання.

### Приклад 1:

Поганий підхід:

```python
class User:
    def __init__(self, name: str):
        self.name = name

    def get_user_data(self):
        pass  # fetch user data from the database

    def save_user_data(self):
        pass  # save user data to the database

    def generate_display_string(self):
        return f"User: {self.name}"
```

У цьому прикладі клас `User` має відповідальність як за отримання/збереження даних користувача, так і за генерацію рядка для відображення.

Кращий підхід:

```python
class User:
    def __init__(self, name: str):
        self.name = name

class UserDataBase:
    @staticmethod
    def get_user_data(user: User):
        pass  # fetch user data from the database

    @staticmethod
    def save_user_data(user: User):
        pass  # save user data to the database

class UserDisplay:
    @staticmethod
    def generate_display_string(user: User):
        return f"User: {user.name}"
```

Тут ми розділили відповідальності між трьома класами.

### Приклад 2:

Поганий підхід:

```python

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        pass  # logic to draw a rectangle
```

Кращий підхід:


```python

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class RectangleDrawer:
    @staticmethod
    def draw(rectangle: Rectangle):
        pass  # logic to draw a rectangle
```

### Приклад 3:

Поганий підхід:

```python
class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):
        pass  # logic to generate a report

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.content)
```

Кращий підхід:

```python
class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):
        pass  # logic to generate a report

class ReportSaver:
    @staticmethod
    def save_to_file(report: Report, file_path):
        with open(file_path, 'w') as file:
            file.write(report.content)

```

У кожному кращому підході ми розділяємо відповідальності, що дозволяє нам зробити код більш гнучким і менш схильним до помилок.

## 2. O — Open/Closed Principle (OCP)

### Опис:

Програмний код повинен бути відкритим для розширення, але закритим для зміни. Це означає, що поведінка модуля може бути розширена без зміни його коду.

### Приклад 1:

Поганий підхід:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
```

Якщо ми захочемо додати ще одну фігуру, нам доведеться змінювати клас `AreaCalculator`.

Кращий підхід:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()
```

Тепер, щоб додати нову фігуру, нам просто потрібно створити новий клас, який наслідується від `Shape`, без зміни класу `AreaCalculator`.

### Приклад 2:

Поганий підхід:

```python
class Logger:
    def log_to_console(self, message):
        print(message)

    def log_to_file(self, message, filename):
        with open(filename, 'w') as file:
            file.write(message)
```

Кращий підхід:

```python
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'w') as file:
            file.write(message)
```

У кращому підході, якщо ми захочемо додати новий метод логування (наприклад, логування в базу даних), нам потрібно буде лише створити новий клас логера, який реалізує абстрактний метод `log`.

### Приклад 3:

Поганий підхід:

```python
class Discount:
    def apply(self, order_type, price):
        if order_type == "summer":
            return price * 0.9
        elif order_type == "black_friday":
            return price * 0.7
```

Кращий підхід:

```python
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class SummerDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class BlackFridayDiscount(Discount):
    def apply(self, price):
        return price * 0.7
```

У кращому підході, якщо потрібно додати нову знижку, можна створити новий клас, який наслідується від `Discount`, без зміни існуючого коду.

Цей принцип допомагає уникнути непередбачених помилок при зміні існуючого коду і робить систему більш гнучкою для розширення.

## 3. L — Liskov Substitution Principle (LSP)

### Опис:

Об'єкти базового класу повинні мати змогу бути заміненими об'єктами підкласів без втрати функціональності. Простіше кажучи, якщо `B` є підкласом класу `A`, то ми повинні мати змогу використовувати `B` замість `A` без будь-яких проблем.

### Приклад 1:

Поганий підхід:

```python
class Bird:
    def fly(self):
        return "I can fly"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Can't fly")
```

У цьому прикладі `Ostrich` є підкласом `Bird`, але він не може літати, тому метод `fly` кидає виключення. Це порушення LSP.

Кращий підхід:

```python
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return "I can fly"

class Ostrich(Bird):
    def move(self):
        return "I can run"
```

### Приклад 2:

Поганий підхід:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
```

Хоча квадрат і є специфічним видом прямокутника, він має однакові сторони. Підходячи до проблеми таким чином, ми можемо отримати непередбачувану поведінку.

Кращий підхід:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

### Приклад 3:

Поганий підхід:

```python
class Engine:
    def start(self):
        return "Engine started"

class ElectricEngine(Engine):
    def start(self):
        raise Exception("Starts differently")

# Автомобілі
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return f"Car started with: {self.engine.start()}"

class ElectricCar(Car):
    def start(self):
        if isinstance(self.engine, ElectricEngine):
            return "Electric car: Electric engine started with a button"
        else:
            return super().start()

```

Тут `ElectricEngine` є підкласом `Engine`, але він стартує інакше, порушуючи LSP.

Кращий підхід:

```python
from abc import ABC, abstractmethod

# Двигуни
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class GasEngine(Engine):
    def start(self):
        return "Gas engine started"

class ElectricEngine(Engine):
    def start(self):
        return "Electric engine started with a button"


# Автомобілі
class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass

class GasCar(Car):
    def start(self):
        return f"Gas car: {self.engine.start()}"

class ElectricCar(Car):
    def start(self):
        return f"Electric car: {self.engine.start()}"


# Перевірка роботи
gas_engine = GasEngine()
electric_engine = ElectricEngine()

bmw = GasCar(gas_engine)
tesla = ElectricCar(electric_engine)

print(bmw.start())  # Output: Gas car: Gas engine started
print(tesla.start())  # Output: Electric car: Electric engine started with a button

```

LSP забезпечує, що підкласи будуть діяти так, як очікується від базового класу, гарантуючи відсутність несподіваних проблем і помилок.

## 4. I — Interface Segregation Principle (ISP)

### Опис:

Клієнти не повинні бути змушені залежати від інтерфейсів, які вони не використовують. Тобто, краще мати багато специфічних інтерфейсів, ніж один універсальний.

### Приклад 1:

Поганий підхід:

```python
from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Man(Worker):

    def work(self):
        return "Working hard."
    
    def eat(self):
        return "Eating lunch."

class Robot(Worker):

    def work(self):
        return "Working automatically."

    def eat(self):
        raise Exception("Robots don't eat!")
```

В даному прикладі `Robot` змушений реалізувати метод `eat()`, який насправді йому не потрібен.

Кращий підхід:

```python
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Man(Workable, Eatable):

    def work(self):
        return "Working hard."
    
    def eat(self):
        return "Eating lunch."

class Robot(Workable):

    def work(self):
        return "Working automatically."
```

### Приклад 2:

Поганий підхід:

```python
class MultiFunctionDevice(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(MultiFunctionDevice):
    def print(self, document):
        # actual print logic
        pass

    def scan(self, document):
        raise Exception("This device can't scan!")

    def fax(self, document):
        raise Exception("This device can't fax!")
```

Тут `OldPrinter` змушений реалізувати `scan` і `fax`, хоча він цього не робить.

Кращий підхід:


```python
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        # actual print logic
        pass
```

### Приклад 3:

Поганий підхід:

```python
class Bird:
    def fly(self):
        pass
    
    def swim(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying in the sky!"

    def swim(self):
        raise Exception("Sparrow can't swim!")

class Duck(Bird):
    def fly(self):
        return "Flying a short distance."

    def swim(self):
        return "Swimming in the pond!"
```

Тут `Sparrow` змушений реалізувати метод `swim`, який насправді йому не потрібен.

Кращий підхід:


```python
class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmingBird(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        return "Flying in the sky!"

class Duck(FlyingBird, SwimmingBird):
    def fly(self):
        return "Flying a short distance."

    def swim(self):
        return "Swimming in the pond!"
```

ISP допомагає уникнути проблем, пов'язаних із занадто загальними інтерфейсами, і забезпечує більш чистий та гнучкий дизайн.

## 5. D — Dependency Inversion Principle (DIP)

### Опис:

- Високорівневі модулі не повинні залежати від низькорівневих. Обидва повинні залежати від абстракцій.
- Абстракції не повинні залежати від деталей. Деталі повинні залежати від абстракцій.

Тобто, код повинен залежати від абстрактних інтерфейсів, а не від конкретних реалізацій.

### Приклад 1:

Поганий підхід:

```python
class LightBulb:
    def turn_on(self):
        return "LightBulb: Bulb turned on..."
        
    def turn_off(self):
        return "LightBulb: Bulb turned off..."
        
class Switch:
    def __init__(self, bulb):
        self.bulb = bulb
        
    def operate(self):
        return self.bulb.turn_on()
```

Тут `Switch` безпосередньо залежить від конкретного класу `LightBulb`.

Кращий підхід:

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
        
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        return "LightBulb: Bulb turned on..."
        
    def turn_off(self):
        return "LightBulb: Bulb turned off..."

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
        
    def operate(self):
        return self.device.turn_on()
```

### Приклад 2:

Поганий підхід:

```python
class MySQLDatabase:
    def connect(self):
        pass
        
    def disconnect(self):
        pass
        
class Application:
    def __init__(self):
        self.database = MySQLDatabase()
        
    def start(self):
        self.database.connect()
```

Тут `Application` безпосередньо залежить від конкретного класу `MySQLDatabase`.

Кращий підхід:


```python
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
        
    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        pass
        
    def disconnect(self):
        pass
        
class Application:
    def __init__(self, database):
        self.database = database
        
    def start(self):
        self.database.connect()
```

### Приклад 3:

Поганий підхід:

```python
class PDFBook:
    def read(self):
        return "Reading a PDF Book..."

class EBookReader:
    def __init__(self):
        self.book = PDFBook()
        
    def read(self):
        return self.book.read()
```

Тут `EBookReader` безпосередньо залежить від конкретного класу `PDFBook`.

Кращий підхід:

```python
class Book(ABC):
    @abstractmethod
    def read(self):
        pass

class PDFBook(Book):
    def read(self):
        return "Reading a PDF Book..."

class EBookReader:
    def __init__(self, book: Book):
        self.book = book
        
    def read(self):
        return self.book.read()
```

DIP допомагає зробити систему більш гнучкою, легшою для тестування та розвитку, і менш залежною від конкретних реалізацій.
