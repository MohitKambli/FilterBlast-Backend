# FilterBlast-Backend

Welcome to FilterBlast-Backend! 🎨 This repository powers the backend of FilterBlast, an innovative image filtering web application that allows users to upload images, apply trendy filters, and download the filtered images. Built with a modern tech stack, FilterBlast-Backend ensures a seamless, scalable, and efficient image processing experience using cloud storage, serverless technology, and an API-driven architecture.

## 🌟 Features

***Dynamic Image Upload and Filtering***: Users can upload images, which are then stored securely in Amazon S3. Our backend processes the images with popular filters like Hudson, Inkwell, Kelvin, and more, giving each photo a unique aesthetic transformation.

***Efficient AWS Integration***: All image files are stored in AWS S3, ensuring reliable and scalable storage. The backend handles uploading, downloading, and filter transformations with ease.

***Versatile Filter Options***: Our application leverages the Pilgram library to apply popular Instagram-style filters, allowing users to select from a range of visually appealing options.

***Real-Time Download Logging***: Each download is logged with user information, timestamp, and the specific filter applied. The logs are stored in MongoDB, giving insights into usage patterns and providing a record of user interactions.

***Cross-Origin Resource Sharing (CORS)***: Configured to allow secure communication with the React frontend, enabling seamless interactions from various client applications.

## 🚀 Tech Stack

***Flask***: Powers the API and application logic, managing routes for uploading, filtering, and downloading images.

***MongoDB Atlas***: Used for logging download activity, making it easy to store and retrieve data for analytics and user behavior insights.

***AWS S3***: Serves as our primary storage for original and filtered images, ensuring high availability and scalability.

***Pilgram Library***: Applies Instagram-like filters, giving users the ability to stylize images in various ways.

***Python Imaging Library (PIL/Pillow)***: Handles image processing tasks such as opening, transforming, and saving image files.

***Vercel***: Deploys the backend in a serverless, scalable environment with fast performance and low maintenance.

## 🔥 Key Endpoints

***GET /***: Returns a "Hello, World!" message to verify the server is running.

***POST /upload_image***: Receives an image from the client, stores it in S3, applies a range of filters, and returns URLs of the filtered images.

***POST /process_and_fetch***: Applies a selected filter to the uploaded image and returns the filtered image URL.

***GET /download_image***: Downloads a specific image from S3 for the user.

***POST /log_download***: Logs the download activity with user information and timestamp in MongoDB.

## 📑 Getting Started

To run FilterBlast-Backend locally:

Clone the repository:
```
git clone https://github.com/your-username/FilterBlast-Backend.git
cd FilterBlast-Backend
```

Install dependencies:
```
pip install -r requirements.txt
```

Set up environment variables: 
Create a .env file in the root directory and add your configuration:
```
MONGO_URI=your_mongodb_uri
MONGO_DB_NAME=your_database_name
MONGO_COLLECTION_NAME=your_collection_name
AWS_REGION=your_aws_region
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_S3_BUCKET_NAME=your_s3_bucket_name
```

Run the application:
```
python -m api.index
```

## Deploy on Vercel:

Simply push your repository to GitHub and connect it to Vercel. Vercel will automatically deploy the application based on the vercel.json configuration.

## 💡 Inspiration

FilterBlast was created to give users a powerful, flexible way to style their photos. With our easy-to-use interface and fast backend processing, anyone can add flair to their images in seconds, making it ideal for photographers, social media enthusiasts, and anyone looking to give their pictures a personal touch.




