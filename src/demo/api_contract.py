from typing import Any


def create_item_response(item_id: int, name: str) -> tuple[int, dict[str, Any]]:
    return 201, {"id": item_id}
