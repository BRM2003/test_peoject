from django.shortcuts import render
from .models import LogNotes


def add_loges(user, model, description, error_message=''):
    try:
        log_note = LogNotes.objects.create(
            Title=model,
            Description=description,
            error_message=error_message,
            cr_by=user
        )
        log_note.save()
    except Exception as e:
        print(e)


