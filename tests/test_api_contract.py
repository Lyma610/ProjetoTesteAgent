from demo.api_contract import create_item_response


def test_create_item_uses_created_status() -> None:
    status, _payload = create_item_response(7, "keyboard")
    assert status == 201


def test_create_item_payload_matches_contract() -> None:
    _status, payload = create_item_response(7, "keyboard")
    assert payload == {"id": 7, "name": "keyboard", "status": "created"}
