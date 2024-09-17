from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE,
)

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to Kinnect API"
    })
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password1 = data.get('password1')
            password2 = data.get('password2')
            # Validate the data
            if not username or not email or not password1 or not password2:
                return JsonResponse({"error": "All fields are required"}, status=400)
            if password1 != password2:
                return JsonResponse({"error": "Passwords do not match"}, status=400)
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists"}, status=400)
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return JsonResponse({"message": "User registered successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# dj-rest-auth logout view fix
# code from Code Institute’s Django REST framework walkthrough
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response