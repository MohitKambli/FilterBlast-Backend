import boto3
import io
from PIL import Image
from ..config import Config
from .redis_client import redis_client

s3 = boto3.client(
    's3',
    region_name=Config.AWS_REGION,
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
)

bucket_name = Config.AWS_S3_BUCKET_NAME

def upload_image_to_s3(file):
    s3.upload_fileobj(file, bucket_name, file.filename)
    return f"https://{bucket_name}.s3.amazonaws.com/{file.filename}"

def upload_filtered_image_to_s3(output_image, filtered_image_filename):
    s3.upload_fileobj(output_image, bucket_name, filtered_image_filename)
    return f"https://{bucket_name}.s3.amazonaws.com/{filtered_image_filename}"

def delete_all_images_from_s3():
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        keys = [{'Key': obj['Key']} for obj in response['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': keys})

def get_image_from_s3(image_url):
    # Create a cache key based on the image URL
    cache_key = f"image_cache:{image_url.split('/')[-1]}"

    # Check if the image is already cached in Redis
    cached_image_data = redis_client.get(cache_key)
    if cached_image_data:
        # Return the cached image data as a BytesIO stream
        print('Returning from cache')
        return io.BytesIO(cached_image_data)

    # If the image is not cached, retrieve it from S3
    response = s3.get_object(Bucket=bucket_name, Key=image_url.split('/')[-1])
    image_data = response['Body'].read()

    # Cache the image data in Redis with an expiration time (e.g., 1 hour)
    redis_client.setex(cache_key, 3600, image_data)  # 3600 seconds = 1 hour

    # Return the image data as a BytesIO stream
    return io.BytesIO(image_data)
