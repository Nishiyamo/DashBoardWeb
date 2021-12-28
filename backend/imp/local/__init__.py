import pandas as pd

from backend.imp import BaseImporter


class LocalImporter(BaseImporter):

    def read_historic_data(self):
        pd.read_csv(self.file)

    def get_data_info(self):
        check_offline = self._is_existing_ticket() and self._is_existing_ticket()
        if check_offline:
            return self.read_historic_data()
