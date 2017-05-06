from django.conf.urls import url
from .views import comment_thread

app_name = 'comment'

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
]