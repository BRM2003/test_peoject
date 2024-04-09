from django.contrib import admin
from .models import *


@admin.register(Projects)
class Projects(admin.ModelAdmin):
    list_display = ('Title', 'Status', 'Start_date', 'End_date')

    def get_queryset(self, request):
        qs = super(Projects, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
