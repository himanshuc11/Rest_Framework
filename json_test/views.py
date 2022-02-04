import re
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from json_test.models import People
from rest_framework import serializers
from rest_framework import status

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['first', 'last', 'age'] # "__all__"



## 1XX - Informational
## 2XX - Accepted OK
## 3XX - Redirectional
## 4XX - Client Errors
## 5XX - Server Error


# Create your views here.
@api_view(['GET', 'POST'])
def show_people(request):
    if request.method == "GET":
        people = People.objects.all()  # Type is queryset
        native_type = PeopleSerializer(people, many=True) # Type is dictionary(python native), native_type.data
        return Response(native_type.data, status=status.HTTP_200_OK)

    # if request.method == "POST":
    #     data = request.data
    #     first = data['first']
    #     last = data['last']
    #     age = data['age']

    #     person = People(first=first, last=last, age=age)
    #     person.save()

    #     return Response(data)

    if request.method == "POST":
        # request.data is actually a dictionary
        d = request.data
        # Convert to People object, Deserialization
        person = PeopleSerializer(data=d)
        if person.is_valid():
            person.save()
        else:
            return Response(person.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(person.data, status=status.HTTP_201_CREATED)


# Authenticated User: Check if the user is really who he says he is
# Authorized User: Check if the authenticated user has required permissions to perform the operation(Superuser) 










@api_view(['GET', 'POST'])
def show_detailed(request, person_id):
    if request.method == "GET":
        try:
            person = People.objects.get(id=person_id) # People Object
            serializer = PeopleSerializer(person)
            return Response(serializer.data)
        except People.DoesNotExist:
            return Response('Invalid ID')

    if request.method == "POST":
        return Response('POST ')
    




