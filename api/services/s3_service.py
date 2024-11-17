import boto3
import io
from PIL import Image
from ..config import Config

s3 = boto3.client(
    's3',
    region_name=Config.AWS_REGION,
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
)

bucket_name = Config.AWS_S3_BUCKET_NAME

def upload_image_to_s3(file):
    s3.upload_fileobj(file, bucket_name, file.name)
    return f"https://{bucket_name}.s3.amazonaws.com/{file.name}"

def delete_all_images_from_s3():
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        keys = [{'Key': obj['Key']} for obj in response['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': keys})

def get_image_from_s3(image_url):
    response = s3.get_object(Bucket=bucket_name, Key=image_url.split('/')[-1])
    return io.BytesIO(response['Body'].read())
