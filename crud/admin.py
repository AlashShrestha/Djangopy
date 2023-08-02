from django.contrib import admin
from .models import Blog, Contact

# Register your models here.
admin.site.site_header = "Admin Header"
admin.site.site_title = "Admin Site Title"
admin.site.index_title = "Admin Title"


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user_name",
        "title",
        "sub_heading",
        "content",
    )
    # fields = "title",
    list_editable = (
        "title",
        "sub_heading",
    )
    search_fields = ("user_name",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
