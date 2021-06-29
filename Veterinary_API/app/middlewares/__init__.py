from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.META['Access-Control-Allow-Origin'] = "*"