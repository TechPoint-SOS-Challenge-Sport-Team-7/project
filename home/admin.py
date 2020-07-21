from django.contrib import admin

from .models import Information

admin.site.register(Information)

from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)