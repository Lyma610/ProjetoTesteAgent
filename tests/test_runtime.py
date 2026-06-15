from demo.runtime import display_name, increment_total


def test_missing_user_has_safe_display_name() -> None:
    assert display_name(None) == "anonymous"


def test_increment_total_uses_the_input_value() -> None:
    assert increment_total(4) == 5
