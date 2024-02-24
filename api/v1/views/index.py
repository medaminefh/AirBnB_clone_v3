#!/usr/bin/python3
"""
Blueprint for the API
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return status"""
    return jsonify({"status": "OK"})
