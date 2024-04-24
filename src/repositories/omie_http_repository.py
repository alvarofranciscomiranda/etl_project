from requests import Session
from datetime import datetime
import pandas as pd
import requests


class OmieHttpRepository:

    urls = {
        "pt": "https://www.omie.es/pt/file-download?parents%5B0%5D=marginalpdbcpt&filename=marginalpdbcpt_",
        "es": "https://www.omie.es/es/file-download?parents%5B0%5D=marginalpdbc&filename=marginalpdbc_"
    }

    def __init__(self):
        self.session = Session()

    def get_market_price_data(self, country: str, date: datetime) -> pd.DataFrame:
        date_request_format = self._get_date_request_format(date)

        url = self.urls.get(country)+date_request_format

        response = self.session.get(url)
        print(response.text)

    @staticmethod
    def _get_date_request_format(date: datetime) -> str:
        return date.strftime("%Y%m%d.1")