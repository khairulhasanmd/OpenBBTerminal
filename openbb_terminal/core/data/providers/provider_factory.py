from openbb_terminal.core.data.providers.polygon import PolygonProvider
from openbb_terminal.core.data.providers.yahoo import YahooProvider

# TODO some sort of registry to dynamically load providers and proper imports
# TODO Create function might not have conditional logic
# TODO implement and publish their provider to the registry to then be available


class ApiFactory:
    @staticmethod
    def create(source: str, api_key: str):
        if source == "polygon":
            return PolygonProvider(api_key=api_key)
        elif source == "yahoo":
            return YahooProvider(api_key=api_key)
        else:
            raise ValueError("API not supported")
