from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_people, name="show_people"),
    path('<int:person_id>/', views.show_detailed, name="show_detailed"),
]
