from django.conf.urls import url
from .views import post_create,post_list,post_detail,post_update,post_delete

app_name = 'posts'

urlpatterns = [
    url(r'^create/$', post_create, name='crate'),
    url(r'^detail/$', post_detail, name='detail'),
    url(r'^list/$', post_list, name='list'),
   	url(r'^update/$', post_update, name='update'),
   	url(r'^delete/$', post_delete, name='delete'),

]