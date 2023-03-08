from typing import Dict
from pydantic import BaseModel


class KeyExecutives(BaseModel):
    key_executives_name: str
    key_executives_title: str
    key_executives_title_since: str
    key_executives_year_born: str


class CompanyProfile(BaseModel):
    active: bool
    cik: str
    composite_figi: str
    currency_name: str
    description: str
    homepage_url: str
    list_date: str
    locale: str
    market: str
    market_cap: int
    name: str
    phone_number: str
    primary_exchange: str
    share_class_figi: str
    share_class_shares_outstanding: int
    sic_code: str
    sic_description: str
    ticker: str
    ticker_root: str
    total_employees: int
    type: str
    weighted_shares_outstanding: int
