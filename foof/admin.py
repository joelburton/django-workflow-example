from django.contrib import admin
from foof.models import Moof


class MoofAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published']
    list_display_links = ['id', 'title']

admin.site.register(Moof, MoofAdmin)
