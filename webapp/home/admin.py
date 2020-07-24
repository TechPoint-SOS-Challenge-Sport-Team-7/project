from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Player
from .models import MovieInfo


admin.site.register(Player)

admin.site.register(MovieInfo)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Item, MyModelAdmin)
