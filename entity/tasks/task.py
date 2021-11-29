import pandas as pd


class Task:
    pass


class EvaluateTask(Task):
    query_stock_id: str
    query_start_date: str
    query_end_date: str
    query_quarter: str

    __financial_statement: pd.DataFrame
    __month_revenue: pd.DataFrame

    def __init__(self, query_stock_id: str = None, query_start_date: str = None, query_end_date: str = None, query_quarter: str = None):
        self.query_stock_id = query_stock_id
        self.query_start_date = query_start_date
        self.query_end_date = query_end_date
        self.query_quarter = query_quarter

    @property
    def financial_statement(self) -> pd.DataFrame:
        return self.__financial_statement

    @financial_statement.setter
    def financial_statement(self, financial_statement: pd.DataFrame):
        self.__financial_statement = financial_statement

    @property
    def month_revenue(self) -> pd.DataFrame:
        return self.__month_revenue

    @month_revenue.setter
    def month_revenue(self, month_revenue: pd.DataFrame):
        self.__month_revenue = month_revenue

    @property
    def last_revenue(self):
        return self.__last_revenue
