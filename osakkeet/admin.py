from django.contrib import admin

from osakkeet.models import Osakkeet


class OsakkeetAdmin(admin.ModelAdmin):
    list_display = ('nimi', 'arvo')
    list_editable = ('arvo',)


admin.site.register(Osakkeet, OsakkeetAdmin)
