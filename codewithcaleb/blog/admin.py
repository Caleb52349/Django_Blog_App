from django.contrib import admin
from django.db.models.fields import PositiveBigIntegerField
from .models import Post

# Register your models here.

admin.site.register(Post)