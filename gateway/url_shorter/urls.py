from django.urls import path
from url_shorter.views import URLView

urlpatterns = [
    path('', URLView.as_view(), name="short-url"),
]
