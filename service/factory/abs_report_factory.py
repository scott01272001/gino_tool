
from fundamental_service import FundamentalService


class ReportFactory:
    
    fundamental_service: FundamentalService
    stock_id: str
    start_date: str
    end_date: str

    def __init__(self, fundamental_service: FundamentalService):
        self.fundamental_service = fundamental_service

    def build(self, instance, stock_id:str, start_date:str, end_date:str):
        return instance.run(stock_id, start_date, end_date)