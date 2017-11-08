from django.contrib import admin

# Register your models here.
from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp','image','read_time']
    list_display_links = ['title']
    list_filter = ['updated', 'timestamp']
    # list_editable = ['title']
    search_fields = ['title', 'content']
    class Meta:
        model = Posts

admin.site.register(Posts,PostModelAdmin)