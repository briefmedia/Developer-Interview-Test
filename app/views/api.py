import json
from flask import Flask, Blueprint, request, Response, render_template, got_request_exception, jsonify, session, abort, make_response, redirect

api = Blueprint('api', __name__)

from database import query

# Status Check
@api.route('/status', methods=['GET'])
def api_index():
    response = Response(json.dumps({ "status": True }), mimetype='application/json')
    return response

# Fetch poll data
@api.route('/poll/<id>', methods=['GET'])
def api_find_poll(id):
    lookup = query("SELECT * from polls WHERE uuid = '%s'" % (id))
    if len(lookup) == 0:
        response = {
            "status": False,
            "error": "Poll not found",
            "data": {}
        }
    else:
        lookup_options = query("SELECT name,votes from poll_options WHERE poll_uuid = '%s'" % (id))
        response = {
            "status": True,
            "error": False,
            "data": {
                "title": lookup[0]['description'],
                "description": lookup[0]['description'],
                "options": lookup_options
            }
        }
    return Response(json.dumps(response), mimetype='application/json')

# Cast a vote
@api.route('/vote/<id>', methods=['POST'])
def api_cast_vote(id):
    response = {
        "status": False,
        "data": {}
    }
    data = json.loads(request.data)
    if 'option' not in data:
        response["error"] = "No Option"
    else:
        lookup = query("SELECT * from polls WHERE uuid = '%s'" % (id))
        if len(lookup) == 0:
            response["error"] = "Poll not found"
        else:
            lookup_options = query("SELECT * from poll_options WHERE poll_uuid = '%s' AND name = '%s'" % (id, data['option']))
            if len(lookup_options) > 0:
                query("UPDATE poll_options SET votes = votes + 1 WHERE poll_uuid = '%s' AND votes = '%s'" % (id, data['option']))
                response = {
                    "status": True,
                    "error": False
                }
            else:
                response["error"] = "Can't find option"
    return Response(json.dumps(response), mimetype='application/json')
