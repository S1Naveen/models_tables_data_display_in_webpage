from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Topic_view)
admin.site.register(Webpage_view)
admin.site.register(Access_view)