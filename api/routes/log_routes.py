from flask import Blueprint, request, jsonify
from ..services.db_service import log_download_entry
import datetime

bp = Blueprint('log_routes', __name__)

@bp.route('/log_download', methods=['POST'])
def log_download():
    user_name = request.json.get('userName')
    image_name = request.json.get('imageName')
    timestamp = datetime.datetime.now()
    success, message = log_download_entry(user_name, image_name, timestamp)
    if success:
        return jsonify({"message": message}), 201
    else:
        return jsonify({"error": message}), 500
