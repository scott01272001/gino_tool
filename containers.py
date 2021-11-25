from dependency_injector import containers, providers

from integration.finMind_datasource import FinMindDatasource
from integration import finMind_datasource


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=['config.yml'])

    datasource = providers.Factory(FinMindDatasource)

    finMind_datasource = providers.Singleton(finMind_datasource)
