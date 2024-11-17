import io
from PIL import Image
import pilgram
from .s3_service import upload_image_to_s3, get_image_from_s3

filters = ['hudson', 'inkwell', 'kelvin', 'lark', 'lofi', 'moon', 'perpetua', 'toaster']

def apply_filters(image_url):
    filtered_image_urls = []
    for filter_type in filters:
        filtered_image_url = apply_filter_helper(image_url, filter_type)
        filtered_image_urls.append(filtered_image_url)
    return filtered_image_urls

def apply_filter_helper(image_url, filter_type):
    image_data = get_image_from_s3(image_url).getvalue()
    image = Image.open(io.BytesIO(image_data))
    filtered_image = getattr(pilgram, filter_type)(image)
    output_image = io.BytesIO()
    filtered_image.save(output_image, format='JPEG')
    output_image.seek(0)
    return upload_image_to_s3(output_image)
