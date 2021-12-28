import yfinance as yf

from backend.imp import BaseImporter


class StockImporter(BaseImporter):

    def get_historic_data(self):
        data = yf.download(self.index, start=self.start_date, end=self.end_date)
        self.save_csv_data(data)

    def save_csv_data(self, data):
        with open(self.file, 'w', encoding='UTF8') as f_csv:
            data.to_csv(f_csv)
