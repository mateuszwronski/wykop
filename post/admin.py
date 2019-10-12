from django.contrib import admin
from post.models import Post


# jak wyrzucić z edycji posta date utworzenia dwa sposoby:
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'text', 'author']

# ?drugi sposób?
class PostAdmin(admin.ModelAdmin):
    exclude = ['created']
    list_display = ['title', 'author', 'created']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)

# Register your models here.
