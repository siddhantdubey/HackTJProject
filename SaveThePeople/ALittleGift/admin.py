from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Dogooders, Samaritans, Request


admin.site.register(Dogooders)
admin.site.register(Samaritans)
admin.site.register(Request)
