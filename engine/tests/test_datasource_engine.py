import pytest
from adapter.datasource_adapter.finMind_datasource_adapter import FinMindDatasourceAdapter
from containers import Container
from engine.datasource_engine import DatasourceEngine
from entity.tasks.task import EvaluateTask


class TestDatasourceEngine:

    @pytest.fixture
    def container(self):
        container = Container()
        return container

    def test_data_collection(self, container: Container):
        adapter: FinMindDatasourceAdapter = container.finMind_adapter.provided()
        engine: DatasourceEngine = DatasourceEngine(adapter)
        task: EvaluateTask = EvaluateTask(
            '2330', '2020-10-01', '2020-11-30', '2020-4')
        task = engine.run(task)
        print(task.month_revenue)
        print(task.financial_statement)

        assert not task.month_revenue.empty and not task.financial_statement.empty
