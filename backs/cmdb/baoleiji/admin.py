from django.contrib import admin
from .models import *
# Register your models here.


class bind_users_hosts_zdy(admin.ModelAdmin):
    filter_horizontal = ("hosts_id",)









admin.site.register(idc)
admin.site.register(hosts)
admin.site.register(bind_users_hosts,bind_users_hosts_zdy)
admin.site.register(shenji)
admin.site.register(mulu_sfile_dfile)
admin.site.register(gongong_shell)
