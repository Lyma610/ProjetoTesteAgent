from typing import Any


def create_item_response(item_id: int, name: str) -> tuple[int, dict[str, Any]]:
    return 200, {"id": item_id, "name": name, "status": "created"}
