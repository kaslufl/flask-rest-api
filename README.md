
# flask-rest-api

---

A basic Python REST API with a flask SQL-Alchemy database.

### 🎯 endpoints:

To add a new video:

👉 **PUT** video/<video_id>?title={title}&views={views}&likes={likes}

To patch a video:

👉 **PATCH** video/<video_id>?title={title}&views={views}&likes={likes}

To delete a video:

👉 **DELETE** video/<video_id>

To get a video:

👉 **GET** video/<video_id>

### ⚙️ requirements:

aniso8601==8.0.0

click==7.1.2

Flask==1.1.2

Flask-RESTful==0.3.8

Flask-SQLAlchemy==2.4.3

itsdangerous==1.1.0

Jinja2==2.11.2

MarkupSafe==1.1.1

pytz==2020.1

six==1.15.0

SQLAlchemy==1.3.18

Werkzeug==1.0.1