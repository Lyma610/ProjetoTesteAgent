from collections.abc import Mapping


def display_name(user: Mapping[str, str] | None) -> str:
    if user is None:
        return "anonymous"
    return user["name"]


def increment_total(value: int) -> int:
    return value + 1
