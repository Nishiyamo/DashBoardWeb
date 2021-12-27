from datetime import datetime
import time
import json

ROOT_FILE_DIRECTORY = 'offline_assets/'


class Offline:

    # By default this importer is going to take the values from the actual year from 'yahoo' api of Amazon ticker
    def __init__(self, file=None, index=None, start_date=None, end_date=None):
        self.file = file
        self.index = index or 'AMZN'
        self.start_date = start_date or datetime.datetime(int(time.strftime('%Y')), 1, 1).strftime("%Y-%m-%d")
        self.end_date = end_date or datetime.date.today().strftime("%Y-%m-%d")

    def read_historic_data(self):
        file_directory = ROOT_FILE_DIRECTORY + self.file
        with open(file_directory) as file_json:
            return json.load(file_json)

