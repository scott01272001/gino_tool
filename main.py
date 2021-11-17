from FinMind.data import DataLoader
from fundamental_service import FundamentalService
from google_sheet_service import SheetService

user_id:str = 'scott0127'
password:str = 'yu82618220'
stock_id: str = '2330'
start_date: str = '2021-11-01'
end_date: str = '2021-11-16'

api = DataLoader()
api.login(user_id, password)
fundamental_service = FundamentalService(api)

# data = fundamental_service.get_stock_month_revenue(stock_id, start_date, end_date)
# print(data.iloc[-10:])

data = fundamental_service.get_taiwan_stock_financial_statement(stock_id, start_date, end_date)
print(data.iloc[-17:])

# sheet_service = SheetService()
# print(type(sheet_service.scoped_credentials))