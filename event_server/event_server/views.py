from django.http import JsonResponse

def custom_404(request, exception):
    return JsonResponse(
        {"status": 404, "error": "Not Found"},
        status=404
    )

def custom_500(request):
    return JsonResponse(
        {"status": 500, "error": "Server Error"},
        status=500
    )

def custom_503(request, exception=None):
    return JsonResponse(
        {"status": 503, "error": "Service Unavailable"},
        status=503
    )



def test_error(request):
    1 / 0   # force a crash on purpose
