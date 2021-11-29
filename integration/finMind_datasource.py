from FinMind.data.data_loader import DataLoader
from integration.datasource_interface import DatasourceInterface
from loguru import logger
import pandas as pd


class FinMindDatasource(DatasourceInterface):

    __data_loader: DataLoader

    def __init__(self, user_id: str, password: str):
        init_success = self._data_loader_init(user_id, password)
        if not init_success:
            logger.error('Init finMind data loader failed.')

    def _data_loader_init(self, user_id: str, password: str) -> bool:
        data_loader = DataLoader()
        success = data_loader.login(user_id, password)
        if success:
            self.__data_loader = data_loader
            return True
        else:
            return False

    def get_financial_statement(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> pd.DataFrame:
        data = self.__data_loader.taiwan_stock_financial_statement(
            stock_id=stock_id, start_date=start_date, end_date=end_date, timeout=timeout)
        return data

    def get_month_revenue(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> pd.DataFrame:
        data = self.__data_loader.taiwan_stock_month_revenue(
            stock_id=stock_id, start_date=start_date, end_date=end_date, timeout=timeout)
        return data
