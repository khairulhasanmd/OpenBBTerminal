from openbb_terminal.core.data.providers.polygon import PolygonProvider
from openbb_terminal.core.data.providers.yahoo import YahooProvider


class ApiFactory:
    @staticmethod
    def create(api: str):
        if api == "polygon":
            return PolygonProvider()
        elif api == "yahoo":
            return YahooProvider()
        else:
            raise ValueError("API not supported")
