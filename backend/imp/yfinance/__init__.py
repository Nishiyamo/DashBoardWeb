import pandas as pd
from datetime import datetime

import yfinance as yf
from backend.settings import ROOT_FILE_DIRECTORY


class StockImporter:

    # By default this importer is going to take the values from the actual year from 'yahoo' api of Amazon ticker
    def __init__(self, index=None, start_date=None, end_date=None):
        self.index = index or 'AMZN'
        self.start_date = start_date or datetime(datetime.today().year, 1, 1).strftime("%Y-%m-%d")
        self.end_date = end_date or datetime.today().strftime("%Y-%m-%d")

    def get_historic_data(self):
        data = yf.download(self.index, start=self.start_date, end=self.end_date)
        self.save_csv_data(data)

    def save_csv_data(self, data):
        file = ROOT_FILE_DIRECTORY + f'/ticker_{self.index}.csv'
        with open(file, 'w', encoding='UTF8') as f_csv:
            data.to_csv(f_csv)
