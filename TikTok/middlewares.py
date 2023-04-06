from rest_framework import status
from rest_framework.request import Request
from django.utils import timezone
from rest_framework.response import Response


class LastActiveMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        response = self.get_response(request)

        user = request.user

        if user.is_authenticated:
            user.last_seen = timezone.now()
            user.save()

        return response


class BannedUserMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        user = request.user
        if user.is_authenticated and user.is_blocked:
            return Response(status=status.HTTP_403_FORBIDDEN)

        response = self.get_response(request)
        return response
