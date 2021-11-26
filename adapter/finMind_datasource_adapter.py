from typing import Callable, Dict
from dependency_injector.wiring import Provide, inject
from pandas.core.frame import DataFrame
from integration.finMind_datasource import FinMindDatasource
from integration.datasource_interface import DatasourceInterface
from dependency_injector.wiring import Provide
from containers import Container
import pandas as pd
from datetime import date


class FinMindDatasourceAdapter:

    _datasource_interface: DatasourceInterface
    _quarter_month_map: Dict[str, int] = {'1': 3, '2': 6, '3': 9, '4': 12}

    def __init__(self, datasource_interface: DatasourceInterface) -> None:
        self._datasource_interface = datasource_interface

    def get_financial_statement_from_source(self, stock_id: str, year_quarter: str, timeout: int = None) -> DataFrame:
        """
        Parameters
        ----------
        stock_id : str
            query stock id
        year_quarter : str
            year-quarter
        timeout : int
            default = None
        Returns
        ----------
        DataFrame
            Stock financial statements
        """
        start_date: str = self._convert_quarter_to_date(year_quarter)
        data: DataFrame = self._datasource_interface.get_financial_statement(
            stock_id=stock_id, start_date=start_date, end_date=start_date, timeout=timeout)
        return data

    def get_month_revenue_from_source(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> DataFrame:
        """
        Parameters
        ----------
        stock_id : str
            query stock id
        start_date : str
            query start date
        end_date : str
            query end date
        timeout : int
            default = None
        Returns
        ----------
        DataFrame
            Stock month revenue
        """
        data: DataFrame = self._datasource_interface.get_month_revenue(
            stock_id=stock_id, start_date=start_date, end_date=end_date, timeout=timeout)
        return data

    def _convert_quarter_to_date(self, year_quarter: str) -> str:
        query_year = year_quarter.split('-')[0]
        query_quarter = year_quarter.split('-')[1]
        query_month = self._quarter_month_map[query_quarter]
        query_date = date(int(query_year), int(query_month), 30)
        return str(query_date)
