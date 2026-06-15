from demo.missing_service import PrimaryService


def selected_provider() -> str:
    return PrimaryService().provider_name()
