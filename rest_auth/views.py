from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(["GET","POST"])
def user_login(request):
    if request.method == "GET":
        return Response('POST username and password')
    if request.method == "POST":
        print(request.data)
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            token = Token.objects.create(user=user)
            return Response(token.key)
        
        return Response('POST DATA')