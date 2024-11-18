import io
from PIL import Image
import pilgram
from .s3_service import upload_image_to_s3, get_image_from_s3, upload_filtered_image_to_s3
from .redis_client import redis_client

filters = ['hudson', 'inkwell', 'kelvin', 'lark', 'lofi', 'moon', 'perpetua', 'toaster']

def apply_filters(image_url):
    filtered_image_urls = []
    for filter_type in filters:
        filtered_image_url = apply_filter_helper(image_url, filter_type)
        filtered_image_urls.append(filtered_image_url)
    return filtered_image_urls

def apply_filter_helper(image_url, filter_type):
    # Create a cache key based on image_url and filter_type
    cache_key = f"{image_url}_{filter_type}"

    # Check if the filtered image URL is already in the cache
    cached_url = redis_client.get(cache_key)
    if cached_url:
        return cached_url.decode('utf-8')  # Return the cached URL if found

    image_data = get_image_from_s3(image_url)
    image = Image.open(image_data)
    
    # Apply filter
    if filter_type == 'hudson':
        filtered_image = pilgram.hudson(image)
    elif filter_type == 'inkwell':
        filtered_image = pilgram.inkwell(image)
    elif filter_type == 'kelvin':
        filtered_image = pilgram.kelvin(image)
    elif filter_type == 'lark':
        filtered_image = pilgram.lark(image)
    elif filter_type == 'lofi':
        filtered_image = pilgram.lofi(image)
    elif filter_type == 'moon':
        filtered_image = pilgram.moon(image)
    elif filter_type == 'perpetua':
        filtered_image = pilgram.perpetua(image)
    elif filter_type == 'toaster':
        filtered_image = pilgram.toaster(image)

    # Generate a unique filename for the filtered image
    filtered_image_filename = f"filtered_{filter_type}_{image_url.split('/')[-1]}"

    output_image = io.BytesIO()
    filtered_image.save(output_image, format='JPEG')
    output_image.seek(0)
    filtered_image_url = upload_filtered_image_to_s3(output_image, filtered_image_filename)

    # Cache the filtered image URL with an expiration time (e.g., 1 hour)
    redis_client.setex(cache_key, 3600, filtered_image_url)

    return filtered_image_url