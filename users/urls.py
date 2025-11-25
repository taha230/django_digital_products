
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView, GetTokenView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('get-token/', GetTokenView.as_view())
]
