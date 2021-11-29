from adapter.datasource_adapter.datasource_adapter_interface import DatasourceAdapterInterface
from engine.engine_interface import EngineInterface
from entity.tasks.task import Task, EvaluateTask


class DatasourceEngine(EngineInterface):
    def __init__(self, datasource_adapter: DatasourceAdapterInterface):
        self.__datasource_adapter = datasource_adapter

    @property
    def datasource_adapter(self):
        return self.__datasource_adapter

    @datasource_adapter.setter
    def datasource_adapter(self, adapter):
        self.__datasource_adapter = adapter

    def run(self, task: Task) -> Task:
        if isinstance(task, EvaluateTask):
            task.financial_statement = self.__datasource_adapter.get_financial_statement_from_source(
                task.query_stock_id, task.query_quarter)
            task.month_revenue = self.__datasource_adapter.get_month_revenue_from_source(
                task.query_stock_id, task.query_start_date, task.query_end_date)

        return task
