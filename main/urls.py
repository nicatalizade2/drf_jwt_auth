from django.urls import path, include
from . views import *
urlpatterns = [
    path('list/', CarList.as_view()),
    path('create/', CarCreate.as_view())
]