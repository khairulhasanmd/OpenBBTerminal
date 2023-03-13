from openbb_terminal.core.data.providers.polygon import PolygonProvider
from openbb_terminal.core.data.providers.yahoo import YahooProvider

# Registry mapping provider names to their corresponding classes
registry = {
    "polygon": PolygonProvider,
    "yahoo": YahooProvider
}


class ApiFactory:
    @staticmethod
    def create(source: str, api_key: str):
        provider_class = registry.get(source)
        if provider_class is None:
            raise ValueError("API not supported")
        return provider_class(api_key=api_key)
