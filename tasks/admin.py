from django.contrib import admin
from .models import *


@admin.register(Tasks)
class Tasks(admin.ModelAdmin):
    list_display = ('Project', 'Title', 'Creation_date', 'Deadline_date')

    def get_queryset(self, request):
        qs = super(Tasks, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)