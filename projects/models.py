from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    STATUS_ACTIVE = 'A'
    STATUS_FINISHED = 'F'
    STATUS_CANCELED = 'C'

    PROJECT_STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_FINISHED, 'Finished'),
        (STATUS_CANCELED, 'Canceled'),
    ]

    id = models.AutoField(primary_key=True),
    Title = models.CharField(max_length=256, unique=True)
    Description = models.TextField()
    Start_date = models.DateTimeField(auto_now=True)
    End_date = models.DateTimeField()
    Status = models.CharField(max_length=1, choices=PROJECT_STATUS_CHOICES, default=STATUS_ACTIVE)

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

    def __str__(self):
        return self.Title





