import abc


class DatasourceInterface(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get_financial_statement(self, stock_id: str, start_date: str, end_date: str, timeout: int = None):
        'get stock quarter financial statement information.'
        return NotImplemented

    @abc.abstractclassmethod
    def get_month_revenue(self, stock_id: str, start_date: str, end_date: str, timeout: int = None):
        'get stock month revenue information.'
        return NotImplemented
