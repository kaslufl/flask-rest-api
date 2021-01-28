from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=True)
    likes = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Video(title ={title}, views = {views}, likes = {likes})"

#db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("title", type=str, help="Needs a title for the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video")
video_put_args.add_argument("likes", type=int, help="Likes on the Video")

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, title = args['title'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201 #Created

    """def delete(self, video_id):
        abort_id_not_exist(video_id)
        del videos[video_id]
        return '', 204 #Deleted"""


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)