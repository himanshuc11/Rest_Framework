from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/', include('json_test.urls')),
    path('auth/', views.obtain_auth_token),
    # path('auth/', include('rest_auth.urls')),
]

