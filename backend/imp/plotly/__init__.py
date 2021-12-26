from datetime import datetime
import time


class PlotlyImporter:

    # By default this importer is going to take the values from the actual year from 'yahoo' api of Amazon ticker
    def __init__(self, index=None, api=None, start_date=None, end_date=None):
        self.index = index or 'AMZN'
        self.api = api or 'yahoo'
        self.start_date = start_date or datetime.datetime(int(time.strftime('%Y')), 1, 1)
        self.end_date = end_date or datetime.date.today()