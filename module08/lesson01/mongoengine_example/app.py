import argparse
from functools import wraps

from mongoengine import *

db = connect(host="mongodb://localhost:27017", db="test")

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class Cat(Document):
    name = StringField(max_length=120, required=True)
    age = IntField(min_value=1, max_value=30)
    features = ListField(StringField(max_length=30))


class ValidationError(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ValidationError(f'Вхідні данні не валідні: {func.__name__}{args}')
        result = func(*args)
        return result

    return wrapper


def find_by_id(pk):
    try:
        result = Cat.objects.get(id=pk)
        return result
    except DoesNotExist:
        return "Документ не найден"

@validate
def create(name, age, features):
    result = Cat(name=name, age=age, features=features)
    result.save()
    return result


@validate
def find():
    r =Cat.objects.all()
    print(Cat.objects.as_pymongo())
    return r


@validate
def update(pk, name, age, features):
    cat = Cat.objects.get(id=pk)
    cat.update(name=name, age=age, features=features)
    return cat


@validate
def remove(pk):
    cat = Cat.objects.get(id=pk)
    cat.delete()
    return cat


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                print(r.to_mongo().to_dict())
            case 'find':
                r = find()
                [print(el.to_mongo().to_dict()) for el in r]
            case 'update':
                r = update(_id, name, age, features)
                print(r.to_mongo().to_dict())
            case 'remove':
                r = remove(_id)
                print(r.to_mongo().to_dict())
            case _:
                print('Unknowns command')
    except ValidationError as err:
        print(err)
    except DoesNotExist:
        print("Документ не найден")


if __name__ == '__main__':
    main()
    # print(find_by_id("6499b6b23058b87bd04e0ddb"))
    # print(find_by_id("6499ba8236f0342efd46ec5f").to_mongo().to_dict())

    # Если вы не уверены, что документ с таким ID существует, вы можете использовать метод first вместо get.
    # Если документ не найден, first просто вернет None, не вызывая исключения:
    doc = Cat.objects(id='6499b6b23058b87bd04e0ddb').first()
    if doc is None:
        print("Документ не найден")

