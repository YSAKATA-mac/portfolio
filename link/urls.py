from django.urls import path
from . import views


urlpatterns = [
    path('', views.link.as_view(), name='link'),
]
