import json

from flask import request
from flask_restful import Resource, fields, marshal_with

import backend.imp.yfinance as yf

finance_fields = {
    'index': fields.String,
}


class YfinanceApi(Resource):
    @marshal_with(finance_fields)
    def get(self):
        params = request.args
        index = params.get('index')
        start_date = params.get('start_date')
        end_date = params.get('end_date')
        stock = yf.StockImporter(index=index, start_date=start_date, end_date=end_date)
        stock.get_historic_data()
