from flask import request
from flask_restful import Resource, fields

import backend.imp.yfinance as yf

finance_fields = {
    'index': fields.String,
}


class YfinanceApi(Resource):
    @staticmethod
    def get(index, start_date=None, end_date=None):
        params = request.args
        start_date = params.get('start_date') or None
        end_date = params.get('end_date') or None
        stock = yf.StockImporter(index=index, start_date=start_date, end_date=end_date)
        stock.get_historic_data()
