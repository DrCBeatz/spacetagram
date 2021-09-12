from django.urls import path

from spacetagram.views import Spacetagram

urlpatterns = [
    path('', Spacetagram.as_view(), name='spacetagram')
]