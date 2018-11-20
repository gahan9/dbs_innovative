from django.contrib import admin

from collection.models import Title


class TitleAdmin(admin.ModelAdmin):
    search_fields = ["title_id", "title", "region", "language"]
    list_display = ["title_id", "title", "ordering", "region", "language", "types", "attributes", "description"]


admin.site.register(Title, TitleAdmin)
