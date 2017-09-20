from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['user', 'content_type', 'timestamp', 'object_id']
	
	class Meta:
		model = Comment

admin.site.register(Comment,CommentModelAdmin)