from flask_restful import Resource, reqparse, abort

videos = {}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("title", type=str, help="Needs a title for the Video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video")
video_put_args.add_argument("likes", type=int, help="Likes on the Video")

def abort_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video not found...")#Not found

def abort_id_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exist with that id...")#Already exist

class Video(Resource):
    def get(self, video_id):
        abort_id_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #Created

    def delete(self, video_id):
        abort_id_not_exist(video_id)
        del videos[video_id]
        return '', 204 #Deleted