from django.contrib import admin
from motd.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date')

admin.site.register(Post, PostAdmin)