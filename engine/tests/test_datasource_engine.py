import pytest
from adapter.datasource_adapter.finMind_datasource_adapter import FinMindDatasourceAdapter
from containers import Container
from engine.datasource_engine import DatasourceEngine
from entity.task.task import EvaluateTask


class TestDatasourceEngine:

    @pytest.fixture
    def container(self):
        container = Container()
        return container

    def test_evaluate_task(self, container: Container):
        adapter: FinMindDatasourceAdapter = container.finMind_adapter.provided()
        engine: DatasourceEngine = DatasourceEngine(adapter)
        task: EvaluateTask = EvaluateTask(
            '2330', '2020-11-01', '2020-11-30', '2020-4')
        task = engine.run(task)
