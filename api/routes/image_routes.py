from flask import Blueprint, request, jsonify, send_file
from ..services.s3_service import upload_image_to_s3, delete_all_images_from_s3, get_image_from_s3
from ..services.filter_service import apply_filters

bp = Blueprint('image_routes', __name__)

@bp.route('/upload_image', methods=['POST'])
def upload_image():
    delete_all_images_from_s3()
    file = request.files['image']
    image_url = upload_image_to_s3(file)
    filtered_image_urls = apply_filters(image_url)
    return jsonify({'uploaded_image_url': image_url, 'filtered_images': filtered_image_urls})

@bp.route('/process_and_fetch', methods=['POST'])
def process_and_fetch():
    data = request.json
    image_url = data['uploaded_image_url']
    selected_filter_index = data['selected_filter_index']
    filtered_image_url = apply_filters(image_url, index=selected_filter_index)
    return jsonify({'filtered_image_url': filtered_image_url})

@bp.route('/download_image', methods=['GET'])
def download_image():
    image_url = request.args.get('image_url')
    return send_file(get_image_from_s3(image_url))
