from django.contrib import admin


from django.contrib import admin
from .models import Food, Comment, Reply

admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(Reply)