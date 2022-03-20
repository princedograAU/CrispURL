from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('short-url/', include('url_shorter.urls'), name="short-url"),
]
