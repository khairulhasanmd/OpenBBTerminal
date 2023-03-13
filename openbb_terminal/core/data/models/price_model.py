import pandas as pd
from openbb_terminal.core.data.providers.provider_factory import ApiFactory
from openbb_terminal.core.data.schemas.prices_schema import StockPrice, IndexPrice
from openbb_terminal.core.data.helpers import validate_df


class PriceDataModel:
    """OpenBB stock object"""

    def __init__(self):
        # metadata
        self.source = None
        self.symbol = None
        self.start_date = None
        self.end_date = None
        self.weekly = None
        self.monthly = None
        self.data_frame = None
        self.verified = False

    def load_from_provider(
        self,
        api_key: str,
        source: str,
        sub_category: str,
        symbol: str,
        start_date: str,
        end_date: str,
        weekly: bool,
        monthly: bool,
    ) -> pd.DataFrame:
        """Load stock data from API

        Args:
            api_key (str): api to use
            symbol (str): stock symbol
            start_date (str): start date
            end_date (str): end date
            weekly (bool): weekly data
            monthly (bool): monthly data

        Returns:
            pd.DataFrame: stock data from API
        """
        self.source = source
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.weekly = weekly
        self.monthly = monthly

        api_provider = ApiFactory.create(self.source, api_key)

        self.data_frame = api_provider.load_stock_data(
            symbol=self.symbol,
            start_date=self.start_date,
            end_date=self.end_date,
            weekly=self.weekly,
            monthly=self.monthly,
        )

        # check data based on sub_category and schema
        if sub_category == "stock_price":
            result, msg = validate_df(self.data_frame, StockPrice)
        elif sub_category == "index_price":
            result, msg = validate_df(self.data_frame, IndexPrice)
        if result is False:
            self.verified = False
            self.data_frame = None
            print(msg)
        else:
            self.verified = True
            print(msg)

    def load_from_file(self, file_path: str) -> pd.DataFrame:
        pass

    def load_from_sql(self, sql_query: str) -> pd.DataFrame:
        pass
