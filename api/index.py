from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import boto3
import io
import pilgram
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'


# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://mohitkambli8:Euphie017119%23@mongodbcluster.q3xfw.mongodb.net/FilterBlastDB?retryWrites=true&w=majority&appName=MongoDBCluster"

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client.get_database('FilterBlastDB')  # Specify the database name
filterblast_collection = db.get_collection('filterblast_collection')  # Specify the collection name

# Initialize AWS S3 client
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id='AKIA6ODU2UVAROXT5ZEE', aws_secret_access_key='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')
bucket_name = 'filter-blast-bucket'

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Delete all objects (images) from the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        keys = [{'Key': obj['Key']} for obj in response['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': keys})

    # Receive image from React app
    file = request.files['image']

    # Upload the image to S3
    s3.upload_fileobj(file, bucket_name, file.filename)
    image_url = f"https://{bucket_name}.s3.amazonaws.com/{file.filename}"

    # Generate filtered images
    filters = ['hudson', 'inkwell', 'kelvin', 'lark', 'lofi', 'moon', 'perpetua', 'toaster']
    filtered_image_urls = []
    for filter_type in filters:
        filtered_image = apply_filter_helper(image_url, filter_type)
        filtered_image_urls.append(filtered_image)

    return jsonify({'uploaded_image_url': image_url, 'filtered_images': filtered_image_urls})

def apply_filter_helper(image_url, filter_type):
    # Download image from S3
    print("URL: ", image_url)
    response = s3.get_object(Bucket=bucket_name, Key=image_url.split('/')[-1])
    image_data = response['Body'].read()
    image = Image.open(io.BytesIO(image_data))

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

    # Upload the filtered image to S3
    output_image = io.BytesIO()
    filtered_image.save(output_image, format='JPEG')
    output_image.seek(0)
    s3.upload_fileobj(output_image, bucket_name, filtered_image_filename)

    # Return the URL of the filtered image
    return f"https://{bucket_name}.s3.amazonaws.com/{filtered_image_filename}"

@app.route('/process_and_fetch', methods=['POST'])
def process_and_fetch():
    data = request.json
    image_url = data['uploaded_image_url']
    selected_filter_index = data['selected_filter_index']
    selected_filter = ['hudson', 'inkwell', 'kelvin', 'lark', 'lofi', 'moon', 'perpetua', 'toaster'][selected_filter_index]
    filtered_image = apply_filter_helper(image_url, selected_filter)
    return jsonify({'filtered_image_url': filtered_image})

@app.route('/download_image', methods=['GET'])
def download_image(user_name, image_name):
    image_url = request.args.get('image_url')

    # Download image from S3
    response = s3.get_object(Bucket=bucket_name, Key=image_url.split('/')[-1])

    # Send image file for download
    return send_file(io.BytesIO(response['Body'].read()))

@app.route('/log_download', methods=['POST'])
def log_download():
    # Get data from the request (user_name and image_name)
    user_name = request.json.get('userName')
    image_name = request.json.get('imageName')
    #timestamp = datetime.datetime.now()

    # Prepare the data to be inserted
    download_log = {
        "user_name": user_name,
        "image_name": image_name
    }

    print("Hello World", download_log)

    try:
        # Insert data into MongoDB collection
        filterblast_collection.insert_one(download_log)
        return jsonify({"message": "Download logged successfully!"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": f"Error: {str(e)}"}), 500