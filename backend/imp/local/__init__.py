import pandas as pd

from backend.imp import BaseImporter


class LocalImporter(BaseImporter):

    def read_historic_data(self):
        file = self.file
        pd.read_csv(file)

    def get_data_info(self):
        return self.read_historic_data()

    def print_data(self):
        data = self.get_data_info()
        print(data)
