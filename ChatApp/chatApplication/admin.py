from django.contrib import admin
from . import models

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']
class Messages(admin.ModelAdmin):
    list_display = ['room', 'sender', 'message', 'timestamp']

admin.site.register(models.Message, Messages)
admin.site.register(models.Room, RoomAdmin)
