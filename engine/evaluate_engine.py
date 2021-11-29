from engine.engine_interface import EngineInterface
from entity.tasks.task import Task, EvaluateTask


class EvaluateReport:
    last_revenue: int

    def __str__(self):
        return 'last_revenue:' + str(self.last_revenue)


class EvaluateEngine(EngineInterface):

    def __init__(self):
        pass

    def run(self, task: Task):
        if isinstance(task, EvaluateTask):
            self.__evaluate(task)

    def __evaluate(self, task: EvaluateTask):
        financial_statement = task.financial_statement
        month_revenue = task.month_revenue

        report = EvaluateReport()

        last_revenue = month_revenue.iloc[-1].get('revenue')
        report.last_revenue = last_revenue

        index_operating_expenses = financial_statement.index[
            financial_statement['type'] == 'OperatingExpenses']
        operating_expenses = financial_statement['value'].iloc[index_operating_expenses]

        print(operating_expenses)
        print(financial_statement)
