from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^index.html', views.index, name = 'index'),
    url(r'^ingame.html', views.ingame, name = 'ingame'),
    url(r'^join/$', views.signup, name = 'join'),
    url(r'^login/$', views.signin, name = 'login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
