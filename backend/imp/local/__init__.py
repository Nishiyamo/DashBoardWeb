import pandas as pd

from backend.imp import BaseImporter


class LocalImporter(BaseImporter):

    def read_historic_data(self, index=None):
        file = self.file or index.upper()
        pd.read_csv(file)

    def get_data_info(self):
        return self.read_historic_data()
