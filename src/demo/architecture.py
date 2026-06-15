from demo.legacy_service import LegacyService


def selected_provider() -> str:
    return LegacyService().provider_name()
