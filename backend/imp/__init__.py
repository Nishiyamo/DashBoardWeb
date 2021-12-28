import os.path
from datetime import datetime
import pandas as pd

from backend.settings import ROOT_FILE_DIRECTORY


class BaseImporter:

    # By default this importer is going to take the values from the actual year from 'yahoo' api of Amazon ticker
    def __init__(self, index=None, start_date=None, end_date=None):
        self.index = index.upper() or 'aapl'.upper()
        self.start_date = start_date or datetime(datetime.today().year, 1, 1).strftime("%Y-%m-%d")
        self.end_date = end_date or datetime.today().strftime("%Y-%m-%d")
        self.file = ROOT_FILE_DIRECTORY + f'/ticker_{self.index}.csv'

    def _is_existing_ticket(self):
        return os.path.isfile(self.file)

    def _is_updated_ticket(self):
        ticket_data = pd.read_csv(self.file)
        last_line_date = ticket_data.tail(1)
        last_line_date = last_line_date['Date']
        return last_line_date < self.end_date
