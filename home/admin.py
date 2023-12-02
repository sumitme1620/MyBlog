from django.contrib import admin
from .models import Category, Post

# Register your models here.


# For configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "desc", "url", "add_date")
    search_fields = ("title",)


# For configuration of Post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "title", "content", "url")
    search_fields = ("title",)
    list_filter = ("cat",)
    list_per_page = 50

    class Media:
        js = (
            "https://cdn.tiny.cloud/1/9a704gj3u86fr2d846avx2ia774a6zrjmbug4c0igk8rvld6/tinymce/6/tinymce.min.js",
            "JS/script.js",
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
