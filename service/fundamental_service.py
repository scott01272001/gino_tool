from FinMind.data.data_loader import DataLoader
import pandas as pd

class FundamentalService():
    
    _api:DataLoader

    def __init__(self, data_loader: DataLoader):
        self._api = data_loader

    def get_taiwan_stock_financial_statement(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> pd.DataFrame:
        data = self._api.taiwan_stock_financial_statement(stock_id="2330", start_date='2019-01-01')
        return data

    def get_stock_month_revenue(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> pd.DataFrame:
        data = self._api.taiwan_stock_month_revenue(stock_id=stock_id, start_date=start_date, end_date=end_date, timeout=timeout)
        return data
