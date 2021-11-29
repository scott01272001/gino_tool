import pytest
import pandas as pd
from entity.tasks.task import EvaluateTask
from engine.evaluate_engine import EvaluateEngine


class TestEvaluateEngine:

    def test_evaluate(self):
        month_revenue = pd.read_csv('month_revenue.csv')
        financial_statement = pd.read_csv('financial_statement.csv')

        task = EvaluateTask()
        task.financial_statement = financial_statement
        task.month_revenue = month_revenue

        engine = EvaluateEngine()
        engine.run(task)
