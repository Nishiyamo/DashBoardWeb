import pandas as pd

from backend.imp import BaseImporter


class LocalImporter(BaseImporter):

    def _read_historic_data(self):
        file = self.file
        return pd.read_csv(file)

    def get_data_info(self):
        return self._read_historic_data()

    def print_data(self):
        data = self.get_data_info()
        print(data)
