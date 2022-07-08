from django.urls import path
from .views import RegisterAPIVIew, LoginAPIView, UserAPIView, RefreshAPIView,LogoutAPIView


urlpatterns = [
    path('register', RegisterAPIVIew.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
]
