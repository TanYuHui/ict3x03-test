from django.urls import path
from django.views.generic import RedirectView

from views import home


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     # path(route, view, kwargs=None, name=None) << syntax
     path("", home, name="home"),
     path("home", home, name="home"),

]
