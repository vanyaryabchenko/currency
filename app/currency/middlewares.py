from time import time
from currency.models import RequestResponseLog


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time()
        response = self.get_response(request)
        end = time()
        RequestResponseLog.objects.create(path=request.path, request_method=request.method, time=(end-start)*1000)

        return response
