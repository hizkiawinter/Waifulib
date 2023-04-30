from flask import jsonify, Blueprint, request
err = Blueprint('err', __name__)

def response(message):
    return jsonify({'message': message})

@err.app_errorhandler(404)
def not_found(error):
    return response('404 Not Found'), 404

@err.app_errorhandler(403)
def forbidden(error):
    return response('403 Forbidden'), 403

@err.app_errorhandler(400)
def bad_request(error):
    return response('400 Bad Request'), 400

@err.app_errorhandler(415)
def unsup_media_type(error):
    return response('415 Unsupported Media Type')

@err.app_errorhandler(Exception)
def handle_error(error):
    message = error.description if hasattr(error, 'description') else [str(x) for x in error.args]
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return response, error.code if hasattr(error, 'code') else 500