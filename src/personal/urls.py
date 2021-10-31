from django.urls import path, re_path

from personal.views import home_screen_view, chats_screen_view


urlpatterns = [
    path('', home_screen_view, name='home'),
    re_path(r'^(?P<room_id>\d{1,3})/$', chats_screen_view, name='chats'),
]
