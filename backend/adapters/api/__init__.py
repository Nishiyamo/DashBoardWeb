from backend.adapters.api.stock import StockApi


def routes():
    return  {
        '/print/': StockApi
        }
