from django.http import HttpResponseForbidden
import requests


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if 'Authorization' not in request.headers:
                return HttpResponseForbidden("Provide authorization credentials")

            url = "http://127.0.0.1:8001/auth/jwt/verify/"
            r = requests.post(url, data={'token': request.headers['Authorization']})

            if 'detail' in r.json():
                return HttpResponseForbidden("Authorization error: " + r.json()['detail'])
