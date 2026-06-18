from demo.architecture import selected_provider


def test_architecture_imports_an_existing_service() -> None:
    assert selected_provider() == "primary"


def test_architecture_uses_the_primary_dependency() -> None:
    assert selected_provider() != "legacy"
