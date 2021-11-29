from adapter.datasource_adapter.datasource_adapter_interface import DatasourceAdapterInterface
from engine.engine_interface import EngineInterface
from entity.task.task import Task, EvaluateTask


class DatasourceEngine(EngineInterface):
    _datasource_adapter: DatasourceAdapterInterface

    def __init__(self, datasource_adapter: DatasourceAdapterInterface):
        self._datasource_adapter = datasource_adapter

    def run(self, task: Task):
        if isinstance(task, EvaluateTask):
            task.financial_statement = self._datasource_adapter.get_financial_statement_from_source(
                task.query_stock_id, task.query_quarter)
            task.month_revenue = self._datasource_adapter.get_month_revenue_from_source(
                task.query_stock_id, task.query_start_date, task.query_end_date)

    @property
    def datasource_adapter(self):
        return self._datasource_adapter

    @property.setter
    def datasource_adapter(self, adapter):
        self._datasource_adapter = adapter
