from flask import Flask
from flask_restful import Api
from hello_world import HelloWorld
from video import Video

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/helloworld")

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)