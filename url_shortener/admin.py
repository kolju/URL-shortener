from django.contrib import admin

from .models import Link

class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('URL details', {'fields': ['long_url', 'short_url', 'clicks_count']}),
    ]
    list_display = ('short_usl', 'long_url', 'Clicks_count', )


admin.site.register(Link)


'login: admin / pass: qwerty12345'