from demo.primary_service import PrimaryService


def selected_provider() -> str:
    return PrimaryService().provider_name()
