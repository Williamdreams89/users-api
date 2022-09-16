from django.urls import path
from main.api.views import UserAPIView

urlpatterns = [
    path('', UserAPIView.as_view()),
]