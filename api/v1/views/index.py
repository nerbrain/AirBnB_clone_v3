#!/usr/bin/python3
"""
Index File

This module contains routes for retrieving status and statistics information.

Routes:
- /status: Returns JSON with status information.
- /stats: Returns JSON with the count of each instance.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns JSON with status information.

    Returns:
        A JSON response with a "status" key set to "OK".
    """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def countAll():
    """
    Returns JSON with the count of each instance.

    Returns:
        A JSON response with the count of different instances:
        - amenities: Count of "Amenity" instances.
        - cities: Count of "City" instances.
        - places: Count of "Place" instances.
        - reviews: Count of "Review" instances.
        - states: Count of "State" instances.
        - users: Count of "User" instances.
    """
    return jsonify(amenities=storage.count("Amenity"),
            cities=storage.count("City"),
            places=storage.count("Place"),
            reviews=storage.count("Review"),
            states=storage.count("State"),
            users=storage.count("User"))
