from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from deepface import DeepFace
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.conf import settings

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY

@method_decorator(login_required(login_url='base_app:login'), name='dispatch')
class AnalyzeView(View):
    template_name = 'base_app/analyze.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.get('image')
        image_data = base64.b64decode(data.split(',')[1])
        image = Image.open(BytesIO(image_data))
        
        # Convert image to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Analyze the image
        try:
            result = DeepFace.analyze(image_cv, actions=['emotion'])
              # Get the dominant emotion
            emotion = result[0]
            dominant_emotion = emotion['dominant_emotion']
            print()
            print(dominant_emotion)

            # Generate music recommendation using YouTube Data API
            youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=music+{dominant_emotion}&key={YOUTUBE_API_KEY}&maxResults=5"
            youtube_response = requests.get(youtube_url)
            youtube_data = youtube_response.json()
            print(f'\n|||||||||||||||||{youtube_data}||||||||||||||||\n')
            music_recommendation = youtube_data['items'][0]['snippet']['title']
            youtube_link = f"https://www.youtube.com/watch?v={youtube_data['items'][0]['id']['videoId']}"
            
            return JsonResponse({
                "musicRecommendation": music_recommendation,
                "youtubeLink": youtube_link,
                "emotion": dominant_emotion
            })

        except ValueError:
            messages.error(request, 'try again')
            return JsonResponse({
                "emotion": 'No Emotion Could be Detected. No face is found in the capture, please ensure your area is well lighted and  face is visible'
            })

