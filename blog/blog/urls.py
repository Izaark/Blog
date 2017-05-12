from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from user.views import login_view, register_view, logout_view

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^comment/', include("comments.urls")),
	url(r'^login/', login_view, name = 'login' ),
	url(r'^logout/', logout_view, name = 'logout' ),
	url(r'^register/', register_view, name = 'register' ),
	url(r'^', include("Posts.urls")),
	url(r'^api/posts/', include('Posts.api.urls'), name = 'posts-api' ),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

