from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('sampley/',sampley,name='sampley')
]