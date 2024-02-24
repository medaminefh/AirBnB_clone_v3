#!/usr/bin/python3
"""
Flask rest api
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

@app.teardown_appcontext
def close(self):
    """call close method"""
    storage.close()


if __name__ == "__main__":
    """run the app using the env variables"""
    host = os.environ.get('HBNB_API_HOST') or '0.0.0.0'
    port = os.environ.get('HBNB_API_PORT') or 5000
    app.run(host= host, port= port, threaded=True)
