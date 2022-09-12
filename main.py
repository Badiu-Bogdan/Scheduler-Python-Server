from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return F"Video(name={self.name}, views={self.views}, likes={self.likes}"


#db.create_all()

names = {"tim": {"age": 19, "gender": "male"}, "bill": {"age": 70, "gender": "male"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)


class HelloWorld(Resource):
    def get(self, name, test):
        print(request.form)
        return names[name]

    def post(self):
        return {"data": "Posted"}

    def put(self, name, test):
        args = video_put_args.parse_args()
        return {"args": args}


videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form)
        return {}


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
