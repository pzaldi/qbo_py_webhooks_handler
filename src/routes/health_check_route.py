from flask import Blueprint, jsonify

health_check_bp = Blueprint('health_check', __name__)


@health_check_bp.route('/healthz', methods=['GET'])
def healthz():
    """
    Health check endpoint for monitoring.  Returns 200 OK if the application is running.
    """
    return jsonify({'status': 'ok'}), 200