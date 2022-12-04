from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(["POST"])
def get_token(request):
    username = request.data["username"]
    password = request.data["password"]

    # check is username and password are correct
    user = authenticate(username=username, password=password)
    if user is not None:
        # user is valid
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key)

    return HttpResponse(status=401)


@csrf_exempt
@api_view(["POST"])
def create_user(request):
    username = request.data["username"]
    password = request.data["password"]

    if User.objects.filter(username=username).exists():
        return HttpResponse(status=409)

    user = User.objects.create_user(username=username, password=password)
    user.save()

    return HttpResponse(status=200, content="User created")
