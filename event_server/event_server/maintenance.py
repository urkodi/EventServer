from django.http import JsonResponse
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, "MAINTENANCE_MODE", False):
            return JsonResponse({"detail": "Service Unavailable"}, status=503)
        return self.get_response(request)
