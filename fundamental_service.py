from FinMind.data.data_loader import DataLoader
import pandas as pd

class FundamentalService():
    def __init__(self, data_loader: DataLoader):
        self.api = data_loader

    def getData(self, stock_id: str, start_date: str, end_date: str, timeout: int = None,) -> pd.DataFrame:
        data = self.api.taiwan_stock_financial_statement(stock_id="2330", start_date='2019-01-01')
        return data
