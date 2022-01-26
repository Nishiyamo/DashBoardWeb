import os.path
import pandas as pd
from backend.domain.managers import BaseManager


class TicketStatusManager(BaseManager):

    def _is_existing_ticket(self):
        return os.path.isfile(self.file)

    def _is_updated_ticket(self):
        if self._is_existing_ticket():
            ticket_data = pd.read_csv(self.file)
            last_line_date = ticket_data.tail(1)
            last_line_date = last_line_date['Date']
            return last_line_date < self.end_date
        else:
            return False

    def status_manager_ticket(self):
        check_offline = self._is_updated_ticket()
        if check_offline:
            from backend.imp.local import LocalImporter
            offline = LocalImporter(self.index)
            return offline.print_data()
        else:
            from backend.imp.yfinance import StockImporter
            online = StockImporter(self.index)
            online.get_historic_data()
            from backend.imp.local import LocalImporter
            offline = LocalImporter(self.index)
            return offline.print_data()
