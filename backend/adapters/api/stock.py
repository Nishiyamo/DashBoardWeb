from flask import request
from flask_restful import Resource, fields, marshal_with

from backend.domain.managers.status_manager import TicketStatusManager as TSM

finance_fields = {
    'index': fields.String,
    'start_date': fields.String,
    'end_date': fields.String
}


class StockApi(Resource):
    @marshal_with(finance_fields)
    def get(self):
        params = request.args
        index = params.get('index')
        start_date = params.get('start_date') or None
        end_date = params.get('end_date') or None
        stock = TSM(index=index, start_date=start_date, end_date=end_date)
        return stock.status_manager_ticket()
