from django.contrib import admin
from .models import *


@admin.register(Staff)
class Staff(admin.ModelAdmin):
    list_display = ('user', 'Position', 'cr_by', 'cr_on')

    def get_queryset(self, request):
        qs = super(Staff, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Positions)
class Positions(admin.ModelAdmin):
    list_display = ('Title', 'cr_by', 'cr_on')

    def get_queryset(self, request):
        qs = super(Positions, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)