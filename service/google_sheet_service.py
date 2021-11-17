import gspread
from google.oauth2 import service_account

class SheetService:
    key_file:str = './bionic-union-332314-ddbafdf8872c.json'
    scopes:list = ['https://www.googleapis.com/auth/spreadsheets']

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(self.key_file)
        self._scoped_credentials = credentials.with_scopes(self.scopes)

    @property
    def scoped_credentials(self):
        return self._scoped_credentials