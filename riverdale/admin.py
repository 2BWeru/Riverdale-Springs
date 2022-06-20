from django.contrib import admin

from django.contrib import admin
from .models import Neighborhood, Post,User,Images,Business

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Images)
admin.site.register(Post)


