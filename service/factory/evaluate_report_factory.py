
from factory.abs_report_factory import ReportFactory
from fundamental_service import FundamentalService


class EvaluateReportFactory(ReportFactory):
    
    def __init__(self, fundamental_service:FundamentalService):
        super().__init__(fundamental_service)

    def run(self, stock_id:str, start_date:str, end_date:str):
        print('run')