from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from enum import Enum
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class User(db.Model):
    address = db.Column(db.String(12), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    adjList = db.Column(db.String(500), nullable=False)


post_parser = reqparse.RequestParser()
post_parser.add_argument("type", type=int, help="No post type given", required = True)
post_parser.add_argument("name", type=str, help="No name given")
post_parser.add_argument("adjList", type=str, help="No list given")

class POSTTYPE(Enum):
    NEW = 1
    UPD = 2

resource_fields = {
    'address' : fields.String,
    'name' : fields.String,
    'adjList' : fields.String
}
class DataBase(Resource):

    @marshal_with(resource_fields)
    def get(self, a):
        result = User.query.filter_by(address=a).first()
        if not result:
            abort(404, message="Address does not exists")
        return result

    @marshal_with(resource_fields)
    def post(self, a):
        args = post_parser.parse_args()
        result = User.query.filter_by(address=a).first()
        if args["type"] == 1:
            if result:
                abort(409, message="Address already exists")
            user = User(address = a, name = args["name"], adjList = "{ }")
            db.session.add(user)
        elif args["type"] == 2: #"address" : {"time", "location"}
            if not result:
                abort(404, message="User Address does not exists")
            al = json.loads(result.adjList)
            li = json.loads(args["adjList"])
            for key, value in li.items():
                person = User.query.filter_by(address=key)
                if person:
                    al[key] = value
            result.adjList = json.dumps(al)
        db.session.commit()
        return
        
    def delete(self, a):
        result = User.query.filter_by(address=a).first()
        if not result:
            abort(404, message="Address does not exists")
        db.session.delete(result)
        db.session.commit()
api.add_resource(DataBase, "/database/<string:a>")

if __name__== "__main__":
    app.run(debug=True)