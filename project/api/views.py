# project/api/views.py
from flask import Blueprint, jsonify


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'ping blueprint pong'
    })


@users_blueprint.route('/pong', methods=['GET'])
def pong():
    return jsonify({
        'status': 'success',
        'message': 'new route and pong ,essage for testing'
    })
