from django.contrib import admin

# Register your models here.
from .models import Postblog,BlogComment

admin.site.register(Postblog)
admin.site.register(BlogComment)