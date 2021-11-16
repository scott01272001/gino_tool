from FinMind.data import DataLoader
from fundamental_service import FundamentalService

user_id:str = 'scott0127'
password:str = 'yu82618220'
stock_id: str = '2330'
start_date: str = '2021-11-16'
end_date: str = '2021-11-16'

api = DataLoader()
api.login(user_id, password)

fundamental_service = FundamentalService(api)
data = fundamental_service.getData(stock_id, start_date, end_date)
print(data.iloc[-50:])
