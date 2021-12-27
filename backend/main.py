from flask import Flask
from flask_restful import Api
import sys

from backend.adapters.api.yfinance import YfinanceApi

app = Flask(__name__)
api = Api(app)
port = 80

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

api.add_resource(YfinanceApi, '/stock/<index>/<start_date>/<end_date>/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
