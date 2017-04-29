from django.conf.urls import url
from .views import post_create,post_list,post_detail,post_update,post_delete

app_name = 'posts'

urlpatterns = [
    url(r'^create/$', post_create, name='crate'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),	#sólo digitos increment
    url(r'^$', post_list, name='list'),
   	url(r'^update/$', post_update, name='update'),
   	url(r'^delete/$', post_delete, name='delete'),

]