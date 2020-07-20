from django.contrib import admin

from .models import Information
from .models import MovieInfo

admin.site.register(Information)

admin.site.register(MovieInfo)

