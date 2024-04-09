from django.db import models
from django.contrib.auth.models import User


class LogNotes(models.Model):
    Title = models.CharField(max_length=512)
    Description = models.TextField()
    Error_message = models.TextField(null=True, blank=True)
    cr_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='log_cr_by')
    cr_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Log notes'
        verbose_name = 'Log note'

    def __str__(self):
        return self.Title
