from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('short-url/', include('url_shorter.urls'), name="short-url"),
]
