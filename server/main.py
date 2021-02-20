from flask import Flask
from flask_socketio import SocketIO, send
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from enum import Enum
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "jtpdoerenjaraedsk"
socketio = SocketIO(app)
db = SQLAlchemy(app)



class User(db.Model):
    address = db.Column(db.String(12), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    adjList = db.Column(db.String(500), nullable=False)
    covid = db.Column(db.Boolean, nullable=False)

post_parser = reqparse.RequestParser()
post_parser.add_argument("type", type=int, help="No post type given", required = True)
post_parser.add_argument("name", type=str, help="No name given")
post_parser.add_argument("location", type=str, help="No list given")
post_parser.add_argument("time", type=str, help="No time given")
post_parser.add_argument("list", type=str, help = "No help given")
post_parser.add_argument("covid", type=bool, help="No covid boolean given")

class POSTTYPE(Enum):
    NEW = 1
    UPD = 2

resource_fields = {
    'address' : fields.String,
    'name' : fields.String,
    'adjList' : fields.String,
    'covid' : fields.Boolean
}
def dfs(address):
    pass
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
            user = User(address = a, name = args["name"], adjList="{ }", covid=False)
            db.session.add(user)
        elif args["type"] == 2:
            if not result:
                abort(404, message="User Address does not exists")
            al = json.loads(result.adjList)
            for ad in args["list"].split(","):
                person = User.query.filter_by(address=ad).first()
                if person:
                    li = json.loads(person.adjList)
                    al[ad] = {"time":args["time"], "location" : args["location"]}
                    li[a] = {"time":args["time"], "location" : args["location"]}
                    person.adjList = json.dumps(li)
            result.adjList = json.dumps(al)
        elif args["type"] == 3:
            if not result:
                abort(404, message="User Address does not exists")
            if args["covid"] is None:
                abort(404, message="No covid boolean given")
            result.covid = args["covid"]
            if result.covid:
                dfs(a)

        db.session.commit()
        return
       
    def delete(self, a):
        result = User.query.filter_by(address=a).first()
        if not result:
            abort(404, message="Address does not exists")
        db.session.delete(result)
        db.session.commit()

api.add_resource(DataBase, "/database/<string:a>")

if __name__ == "__main__":
    socketio.run(app, debug=True)