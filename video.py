from flask_restful import Resource, reqparse

videos = {}
video_put_args = reqparse.RequestParser()

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        
        return