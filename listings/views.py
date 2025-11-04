from django.http import JsonResponse

def index(request):
    """
    Simple root endpoint to verify the API is working.
    """
    return JsonResponse({"message": "Welcome to ALX Travel Listings API!"})
