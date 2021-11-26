from dependency_injector import containers, providers
from integration import finMind_datasource
from adapter import finMind_datasource_adapter


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(yaml_files=['resource/config.yml'])

    finMind_datasource = providers.Singleton(
        finMind_datasource.FinMindDatasource,
        user_id=config.datasource.finMind.user_id,
        password=config.datasource.finMind.password()
    )

    finMind_adapter = providers.Singleton(
        finMind_datasource_adapter.FinMindDatasourceAdapter,
        datasource_interface=finMind_datasource
    )
