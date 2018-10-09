from django.contrib import admin
from blog.models import Post, Topic

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')

admin.site.register(Post, PostAdmin)
admin.site.register(Topic)