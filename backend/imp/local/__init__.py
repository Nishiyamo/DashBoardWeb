import csv

from backend.imp import BaseImporter


class Local(BaseImporter):

    def read_historic_data(self):
        file_directory = self.file
        with open(file_directory) as file_csv:
            return csv.reader(file_csv)
