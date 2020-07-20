from django.contrib import admin

from .models import Player
from .models import MovieInfo


admin.site.register(Player)

admin.site.register(MovieInfo)

