from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'due_date')
    search_fields = ('title', 'user_username')
    list_filter = ('status', 'created_at', 'due_date')
    
