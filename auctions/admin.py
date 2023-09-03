from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(comment)
admin.site.register(auction)
admin.site.register(bid)

