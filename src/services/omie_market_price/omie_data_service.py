from datetime import datetime, timedelta

import pandas as pd


class OmieDataService:
    def __init__(self, http_repository, mysql_repository):
        self._http_repository = http_repository
        self._mysql_repository = mysql_repository

    def main(self, country: str, start_date: datetime, end_date: datetime=None):
        data = pd.DataFrame()

        if not end_date:
            end_date = start_date

        while start_date <= end_date:
            day_data = self._http_repository.get_market_price_data(country, start_date)
            start_date = start_date + timedelta(days=1)

        # self._mysql_repository.save_data(data, country)
