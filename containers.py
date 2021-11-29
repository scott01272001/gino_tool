from dependency_injector import containers, providers
from integration.finMind_datasource import FinMindDatasource
from adapter.datasource_adapter.finMind_datasource_adapter import FinMindDatasourceAdapter


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=['resource/config.yml'])

    finMind_datasource = providers.Singleton(
        FinMindDatasource,
        user_id=config.datasource.finMind.user_id,
        password=config.datasource.finMind.password
    )

    finMind_adapter = providers.Singleton(
        FinMindDatasourceAdapter,
        datasource_interface=finMind_datasource
    )
