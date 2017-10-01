from django.contrib import admin

from groupchat.models import *

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomGroup)
admin.site.register(RoomMessage)
admin.site.register(Message)