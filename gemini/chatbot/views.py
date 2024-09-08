from django.shortcuts import render
from django.http import JsonResponse
import requests
from dotenv import load_dotenv
import os


load_dotenv()

# Replace with your Gemini API endpoint and API key
GEMINI_API_URL = "https://aistudio.google.com/app/apikey"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        
        # Send the user message to Gemini API
        response = requests.post(
            GEMINI_API_URL,
            headers={
                'Authorization': f'Bearer {GEMINI_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={'text': user_message}
        )
        
        # Get the response from Gemini API
        if response.status_code == 200:
            gemini_response = response.json().get('text')
            return JsonResponse({'response': gemini_response})
        else:
            return JsonResponse({'error': 'Error contacting Gemini API'}, status=response.status_code)

    return render(request, 'home.html')
