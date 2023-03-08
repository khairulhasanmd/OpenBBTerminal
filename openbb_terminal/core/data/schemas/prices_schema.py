from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import numpy as np


class StockPrice(BaseModel):
    Volume: float = Field(alias="Volume")
    Adj_Close: float = Field(alias="Adj Close")
    VolWeight_Avg: Optional[float] = Field(alias="VolWeight Avg")
    Open: float = Field(alias="Open")
    High: float = Field(alias="High")
    Low: float = Field(alias="Low")
    Transactions: Optional[float] = Field(alias="Transactions")
    Close: float = Field(alias="Close")
    date: datetime = Field(alias="date")


class IndexPrice(BaseModel):
    Volume: float = Field(alias="Volume")
    Adj_Close: float = Field(alias="Adj Close")
    VolWeight_Avg: Optional[float] = Field(alias="VolWeight Avg")
    Open: float = Field(alias="Open")
    High: float = Field(alias="High")
    Low: float = Field(alias="Low")
    Transactions: Optional[int] = Field(alias="Transactions")
    Close: float = Field(alias="Close")
    date: datetime = Field(alias="date")
