from flask_restful import Resource, reqparse, abort

videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("title", type=str, help="Needs a title for the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video")
video_put_args.add_argument("likes", type=int, help="Likes on the Video")

def check_id_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video not found...")

class Video(Resource):
    def get(self, video_id):
        check_id_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #Created