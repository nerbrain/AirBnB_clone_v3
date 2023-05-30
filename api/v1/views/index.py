#!/usr/bin/python3
""" Index File"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """ Returns JSON """
    return jsonify(status="OK")

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Return count of each instance"""
   return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User")) 
