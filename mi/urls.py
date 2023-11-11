from mi.views import virat
from django.urls import path

app_name='anything'

urlpatterns=[
    path('virat/' ,virat,name='virat'),
]