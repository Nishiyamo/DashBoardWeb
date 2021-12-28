import os.path
from backend.settings import ROOT_FILE_DIRECTORY


class BaseImporter:

    @staticmethod
    def _is_existing_ticket(index):
        return os.path.isfile(ROOT_FILE_DIRECTORY + f'/ticker_{index}.csv')
