from typing import Dict
from pandas.core.frame import DataFrame
from adapter.datasource_adapter.datasource_adapter_interface import DatasourceAdapterInterface
from integration.datasource_interface import DatasourceInterface
from datetime import date


class FinMindDatasourceAdapter(DatasourceAdapterInterface):

    _datasource_interface: DatasourceInterface
    _quarter_month_map: Dict[str, int] = {'1': 3, '2': 6, '3': 9, '4': 12}

    def __init__(self, datasource_interface: DatasourceInterface) -> None:
        self._datasource_interface = datasource_interface

    def get_financial_statement_from_source(self, stock_id: str, year_quarter: str, timeout: int = None) -> DataFrame:
        start_date: str = self._convert_quarter_to_date(year_quarter)
        data: DataFrame = self._datasource_interface.get_financial_statement(
            stock_id=stock_id, start_date=start_date, end_date=start_date, timeout=timeout)
        return data

    def get_month_revenue_from_source(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> DataFrame:
        data: DataFrame = self._datasource_interface.get_month_revenue(
            stock_id=stock_id, start_date=start_date, end_date=end_date, timeout=timeout)
        return data

    def _convert_quarter_to_date(self, year_quarter: str) -> str:
        query_year = year_quarter.split('-')[0]
        query_quarter = year_quarter.split('-')[1]
        query_month = self._quarter_month_map[query_quarter]
        query_date = date(int(query_year), int(query_month), 30)
        return str(query_date)
