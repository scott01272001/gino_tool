import pandas as pd


class Task:
    pass


class EvaluateTask(Task):
    query_stock_id: str
    query_start_date: str
    query_end_date: str
    query_quarter: str

    # _financial_statement: pd.DataFrame
    # _month_revenue: pd.DataFrame

    def __init__(self, query_stock_id: str, query_start_date: str, query_end_date: str, query_quarter: str):
        self.query_stock_id = query_stock_id
        self.query_start_date = query_start_date
        self.query_end_date = query_end_date
        self.query_quarter = query_quarter

    @property
    def financial_statement(self) -> pd.DataFrame:
        return self._financial_statement

    @property.setter
    def financial_statement(self, financial_statement: pd.DataFrame):
        self._financial_statement = financial_statement

    @property
    def month_revenue(self) -> pd.DataFrame:
        return self._month_revenue

    @property.setter
    def month_revenue(self, month_revenue: pd.DataFrame):
        self._month_revenue = month_revenue
