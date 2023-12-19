from typing import Literal


def draw_line(direction: Literal["horizontal", "vertical"], length: int) -> None:
    if direction == "horizontal":
        print("-" * length)
    elif direction == "vertical":
        for _ in range(length):
            print("|")
    else:
        raise ValueError("Invalid direction")


def get_status_code(response: Literal["success", "error", "pending"]) -> int:
    if response == "success":
        return 200
    elif response == "error":
        return 400
    elif response == "pending":
        return 202
    else:
        raise ValueError("Invalid response")
