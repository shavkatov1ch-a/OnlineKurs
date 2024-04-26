from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'video_id')
    list_display_links = ('user_id', 'video_id')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')
    list_display_links = ('first_name', 'email')


admin.site.register(Client, ClientAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Payment)
admin.site.register(Team)
admin.site.register(Video_Darslar)
admin.site.register(Web_sites)
admin.site.register(Web_images)