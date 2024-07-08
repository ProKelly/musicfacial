# Facial Detection Music Recommender

This project is a web application built using Django that uses facial detection technology to analyze the user's emotions and recommend music based on the detected emotion. The application captures the user's image, detects the dominant emotion using the DeepFace library, and suggests music videos from YouTube that match the emotion.

## Features

- Advanced facial detection and emotion analysis
- Personalized music recommendations based on detected emotions
- User-friendly interface with seamless navigation
- Secure and private image processing

## Technologies Used

- Django
- DeepFace
- OpenCV
- Pillow
- Numpy
- Requests
- Tailwind CSS
- YouTube Data API

## Installation

- Django==5.0.6
- pillow==10.2.0
- numpy==1.24.2
- opencv-python==4.10.0.84
- deepface==0.0.92
- requests==2.31.0
- python-decouple==3.8

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Steps

1. Clone the repository:

*bash*

- git clone https://github.com/ProKelly/musicfacial.git
- cd musicfacial 

2. Create a virtual environment and activate it:

- python -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. pip install -r requirements.txt

- pip install -r requirements.txt

4. Set up the environment variables. Create a .env file in the project root and add the following:

- SECRET_KEY=your_secret_key
- DEBUG=True  # Set to False in production
- ALLOWED_HOSTS=localhost, 127.0.0.1

- YOUTUBE_API_KEY=your_youtube_api_key

5. Apply migrations:

- python manage.py migrate

6. Create a superuser:

- python manage.py createsuperuser

7. run the development server:

- python manage.py runserver

8. pen your browser and go to http://localhost:8000.

### Usage

    1. Log in to the application.
    2. Navigate to the "Analyze" page.
    3. Allow the application to access your camera.
    4. Capture an image of your face.
    5. The application will analyze the image to detect your emotion and recommend music accordingly.

## Project Structure

   - base_app/: Contains the main Django app, including views, templates, and static files.
   - static/: Contains static files (CSS, JavaScript).
   - templates/: Contains HTML templates.
   - requirements.txt: Lists the dependencies required to run the project.
   - manage.py: Django's command-line utility.

### API Keys

This project requires an API key from the YouTube Data API to fetch music recommendations based on detected emotions. To get an API key, follow these steps:

    1. Go to the Google Cloud Console.
    2. Create a new project or select an existing project.
    3. Navigate to the API & Services > Credentials page.
    4. Click "Create credentials" and select "API key".
    5. Copy the generated API key and add it to your .env file.

### Contributing

- Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the existing coding style and include tests for any new features or bug fixes.

### Acknowledgments

   - DeepFace for emotion detection
   - YouTube Data API for fetching music recommendations


