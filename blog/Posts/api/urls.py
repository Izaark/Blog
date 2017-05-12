from django.conf.urls import url
from .views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDestroyAPIView, PostCreateAPIView
app_name = 'posts'

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
	url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/update/$', PostUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<slug>[\w-]+)/destroy/$', PostDestroyAPIView.as_view(), name='destroy'),


	# url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
]