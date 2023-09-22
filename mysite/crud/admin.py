from django.contrib import admin
from .models import *

class GuilhermeModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["title"]}),
        (None,{"fields":["description"]})
    ]
    list_display = ["title"]

admin.site.register(GuilhermeModel,GuilhermeModelAdmin)