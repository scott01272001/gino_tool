import pytest
from adapter.finMind_datasource_adapter import FinMindDatasourceAdapter
from containers import Container
from integration.datasource_interface import DatasourceInterface


class TestFinMindAdapter:

    @pytest.fixture
    def container(self):
        container = Container()
        return container

    def test_get_financial_statement_from_source(self, container: Container):
        # data_source: DatasourceInterface = container.finMind_datasource.provided()
        # adapter: FinMindDatasourceAdapter = FinMindDatasourceAdapter(
        #     data_source)
        # data = adapter.get_financial_statement_from_source('2330', '2021-1')
        # print(data)

        adapter: FinMindDatasourceAdapter = container.finMind_adapter.provided()
        data = adapter.get_financial_statement_from_source('2330', '2021-1')
        print(data)

        assert True
