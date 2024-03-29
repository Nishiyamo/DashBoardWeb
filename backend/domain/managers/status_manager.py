import os.path
import pandas as pd
from backend.domain.managers import BaseManager


class TicketStatusManager(BaseManager):

    def __int__():
        super().__init__()

    def _is_existing_ticket(self):
        return os.path.isfile(self.file)

    def _is_updated_ticket(self):
        if self._is_existing_ticket():
            ticket_data = pd.read_csv(self.file)
            last_line_date = str(ticket_data.tail(1)['Date'].unique()[0])
            return last_line_date < self.end_date

    def _get_offline_data(self):
        from backend.imp.local import LocalImporter
        offline = LocalImporter(self.index)
        return offline.print_data()

    def _get_online_data(self):
        from backend.imp.yfinance import StockImporter
        online = StockImporter(self.index)
        online.get_historic_data()

    def status_manager(self):
        check_offline = self._is_updated_ticket()
        if check_offline:
            self._get_offline_data()
        else:
           self._get_offline_data()
           self._get_offline_data()
