import abc
import pandas as pd


class DatasourceAdapterInterface(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get_financial_statement_from_source(self, stock_id: str, year_quarter: str, timeout: int = None) -> pd.DataFrame:
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
        return NotImplemented

    @abc.abstractclassmethod
    def get_month_revenue_from_source(self, stock_id: str, start_date: str, end_date: str, timeout: int = None) -> pd.DataFrame:
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
        return NotImplemented
