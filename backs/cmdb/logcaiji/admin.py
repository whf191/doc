from django.contrib import admin
from .models import logs





class zdy_logs(admin.ModelAdmin):
    list_display = ['leixing','neirong']
    list_filter = ('leixing',)
    search_fields = ['leixing','neirong']



admin.site.register(logs,zdy_logs)