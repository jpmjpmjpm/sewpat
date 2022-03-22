from django.contrib import admin

from .models import SewingPattern


class SewingPatternAdmin(admin.ModelAdmin):
    pass


admin.site.register(SewingPattern, SewingPatternAdmin)
