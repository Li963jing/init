from django.contrib import admin

# Register your models here.
from Insta.models import Post,InstaUser

admin.site.register(Post)
admin.site.register(InstaUser)