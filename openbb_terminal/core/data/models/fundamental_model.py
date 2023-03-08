import pandas as pd
from openbb_terminal.core.data.providers.provider_factory import ApiFactory
from schemas.fundamentals_schema import CompanyProfile
from openbb_terminal.core.data.helpers import validate_df


class FundamentalDataModel:
    """OpenBB stock object"""

    def __init__(self):
        # metadata
        self.source = None
        self.symbol = None
        self.date = None
        self.data_frame = None
        self.verified = False

    def load_from_provider(
        self,
        api_key: str,
        source: str,
        symbol: str,
        date: str,
    ) -> pd.DataFrame:
        """Load stock data from API

        Args:
            api (str): api to use
            symbol (str): stock symbol

        Returns:
            pd.DataFrame: stock data from API
        """
        self.source = source
        self.symbol = symbol
        self.date = date
        self.data_frame = pd.DataFrame()

        api_provider = ApiFactory.create(self.source)
        self.data_frame = api_provider.load_fundamental_data(
            api_key=api_key,
            symbol=self.symbol,
            date=self.date,
        )

        # check data
        result, msg = validate_df(self.data_frame, CompanyProfile)
        if result is False:
            self.verified = False
            self.data_frame = None
            print(msg)
        else:
            self.verified = True
            print(msg)

        return self.data_frame
