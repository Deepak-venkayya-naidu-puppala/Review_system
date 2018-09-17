from django.urls import path

from . import views

urlpatterns = [
    path('guestbook/',views.index,name='index'),
    path('sign/',views.sign,name='sign'),
]