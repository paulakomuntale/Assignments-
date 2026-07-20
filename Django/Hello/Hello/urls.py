from importlib.resources import path

from django.contrib import admin
from Hello.views import Myfirstproject


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Myfirstproject),
]
