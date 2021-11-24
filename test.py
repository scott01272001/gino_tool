
from integration.datasource_interface import DatasourceInterface
from integration.finMind_datasource import FinMind

fm: DatasourceInterface
fm = FinMind()
fm.get_financial_statement()
