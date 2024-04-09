from django.contrib import admin
from .models import *


@admin.register(LogNotes)
class LogNotes(admin.ModelAdmin):
    list_display = ('Title', 'Error_message', 'cr_by', 'cr_on')

    def get_queryset(self, request):
        qs = super(LogNotes, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)