from django.contrib import admin
from .models import ShortedUrl, AdditionalUserInfo
# Register your models here.
admin.site.register(ShortedUrl)
admin.site.register(AdditionalUserInfo)