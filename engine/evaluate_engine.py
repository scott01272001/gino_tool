from engine.engine_interface import EngineInterface
from entity.tasks.task import Task, EvaluateTask
import numpy as np


class EvaluateReport:
    last_revenue: float
    operating_expenses: float
    gross_margin: float
    tax_rate: float
    income_after_taxes: float
    eps: float

    def __str__(self):
        return 'last_revenue:' + str(self.last_revenue) + ', operating_expenses:' + str(self.operating_expenses) + ', gross_margin:' + str(self.gross_margin) \
            + ', tax_rate:' + \
            str(self.tax_rate) + ', income_after_taxes:' + \
            str(self.income_after_taxes) + ', EPS:' + str(self.eps)


class EvaluateEngine(EngineInterface):
    __denominator: int = 1000000

    def __init__(self):
        pass

    def run(self, task: Task):
        if isinstance(task, EvaluateTask):
            report = self.__build_report(task)

    def __build_report(self, task: EvaluateTask) -> EvaluateReport:
        """
        Generate the information needed for evaluation from finMind’s financial statements.
        """

        def get_value_by_key(key: str) -> float:
            """
            Get the specified value from financial statements.
            """
            index = financial_statement.index[financial_statement['type'] == key]
            if key == 'EPS':
                value = round(financial_statement.iloc[index].get(
                    'value').tolist()[0], 2)
            else:
                value = round(financial_statement.iloc[index].get(
                    'value').tolist()[0]/self.__denominator, 2)
            return value

        financial_statement = task.financial_statement
        month_revenue = task.month_revenue

        report = EvaluateReport()

        last_revenue = round(
            month_revenue.iloc[-1].get('revenue')/self.__denominator, 2)
        report.last_revenue = last_revenue

        operating_expenses = get_value_by_key('OperatingExpenses')
        report.operating_expenses = operating_expenses

        revenue = get_value_by_key('Revenue')
        cost_of_goods_sold = get_value_by_key('CostOfGoodsSold')
        gross_margin = round((revenue - cost_of_goods_sold)/revenue, 2)
        report.gross_margin = gross_margin

        pre_tax_income = get_value_by_key('PreTaxIncome')
        income_after_taxes = get_value_by_key('IncomeAfterTaxes')
        tax_rate = round(income_after_taxes/pre_tax_income, 2)
        report.tax_rate = tax_rate
        report.income_after_taxes = income_after_taxes

        eps = get_value_by_key('EPS')
        report.eps = eps

        return report
