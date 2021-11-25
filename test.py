import sys
from dependency_injector import containers
from containers import Container
from loguru import logger
from integration.datasource_interface import DatasourceInterface
from integration.finMind_datasource import FinMindDatasource
from dependency_injector.wiring import Provide, inject

logger.add(sys.stderr, level="INFO")

data_source: DatasourceInterface


@inject
def main(data_source: DatasourceInterface = Provide[Container.finMind_datasource]) -> None:
    ...


if __name__ == "__main__":
    main()
