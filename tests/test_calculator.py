from demo.calculator import is_above_limit, subtract


def test_subtract_uses_minus_operator() -> None:
    assert subtract(10, 3) == 7


def test_comparison_identifies_values_above_limit() -> None:
    assert is_above_limit(11, 10) is True
    assert is_above_limit(9, 10) is False
