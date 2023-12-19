from typing import TypedDict


class UserInfo(TypedDict):
    user_id: int
    username: str
    email: str
    is_active: bool


def get_user_info(user_id: int) -> UserInfo:
    # Припустимо, що ми отримуємо дані з бази даних або API
    return {
        "user_id": user_id,
        "username": "john_doe",
        "email": "john@example.com",
        "is_active": True,
    }


user = get_user_info(1)
print(user["username"])  # Виведе: john_doe


class OptionalFieldsUser(TypedDict, total=False):
    user_id: int
    age: int


data: OptionalFieldsUser = {"user_id": 1}  # це дійсний
