from django.contrib import admin
from .models import News, Subsection


class SubsectionInline(admin.StackedInline):
    model = Subsection
    extra = 1


@admin.register(News)
class Blog_NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('author', 'publish')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'tags': ('title',)}
    inlines = [SubsectionInline]


admin.site.register(Subsection)