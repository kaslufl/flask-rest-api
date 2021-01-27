from flask_restful import Resource, reqparse

videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("title", type=str, help="Needs a title for the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video")
video_put_args.add_argument("likes", type=int, help="Likes on the Video")

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}