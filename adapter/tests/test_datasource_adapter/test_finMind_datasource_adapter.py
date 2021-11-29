import pytest
from adapter.datasource_adapter.finMind_datasource_adapter import FinMindDatasourceAdapter
from containers import Container


class TestFinMindAdapter:

    @pytest.fixture
    def container(self):
        container = Container()
        return container

    def test_get_financial_statement_from_source(self, container: Container):
        adapter: FinMindDatasourceAdapter = container.finMind_adapter.provided()
        data = adapter.get_financial_statement_from_source('2330', '2021-1')
        print(data)
        assert not data.empty

    def test_get_month_revenue_from_source(self, container: Container):
        adapter: FinMindDatasourceAdapter = container.finMind_adapter.provided()
        data = adapter.get_month_revenue_from_source(
            '2330', '2020-10-01', '2020-11-30')
        print(data)
        assert not data.empty
