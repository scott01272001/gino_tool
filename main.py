from adapter.datasource_adapter.finMind_datasource_adapter import FinMindDatasourceAdapter
from containers import Container
from integration.datasource_interface import DatasourceInterface
from dependency_injector.wiring import Provide, inject


data_source: DatasourceInterface


@inject
def main(data_source: DatasourceInterface = Provide[Container.finMind_datasource]) -> None:

    adapter: FinMindDatasourceAdapter = FinMindDatasourceAdapter(data_source)

    data = adapter.get_financial_statement_from_source('2330', '2021-2')
    print(data)


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])
    main()
