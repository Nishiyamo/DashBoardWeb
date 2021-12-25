from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
cors = CORS(app)
api = Api(app)
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()