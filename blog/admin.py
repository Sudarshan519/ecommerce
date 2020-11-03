from django.contrib import admin
from .models import Blogpost,BlogComment,Post
# Register your models here.
admin.site.register((Blogpost ,BlogComment,Post))
