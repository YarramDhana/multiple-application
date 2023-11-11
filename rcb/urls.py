from rcb.views import second

from django.urls import path

app_name='anything'

urlpatterns=[
    path('second/',second,name='second'),
]