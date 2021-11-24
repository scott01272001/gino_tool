import abc


class DatasourceInterface(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def get_financial_statement(self):
        'get stock quarter financial statement information.'
        return NotImplemented

    @abc.abstractclassmethod
    def get_month_revenue(self):
        'get stock month revenue information.'
        return NotImplemented
