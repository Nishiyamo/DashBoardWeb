from datetime import datetime
import time

import yfinance as yf


class StockImporter:

    # By default this importer is going to take the values from the actual year from 'yahoo' api of Amazon ticker
    def __init__(self, index=None, start_date=None, end_date=None):
        self.index = index or 'AMZN'
        self.start_date = start_date or datetime.datetime(int(time.strftime('%Y')), 1, 1).strftime("%Y-%m-%d")
        self.end_date = end_date or datetime.date.today().strftime("%Y-%m-%d")

    def get_historic_data(self):
        return yf.Ticker(self.index).history(period='1d', start=self.start_date, end=self.end_date)
