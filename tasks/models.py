from django.db import models
from projects.models import Projects
from django.contrib.auth.models import User


class Tasks(models.Model):
    STATUS_NEW = 'N'
    STATUS_UNDERWAY = 'U'
    STATUS_DONE = 'D'
    STATUS_CANCELED = 'C'

    TASK_STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_UNDERWAY, 'Underway'),
        (STATUS_DONE, 'Done'),
        (STATUS_CANCELED, 'Canceled'),
    ]

    id = models.AutoField(primary_key=True),
    Project = models.ForeignKey(Projects, on_delete=models.PROTECT, related_name='project')
    Title = models.CharField(max_length=256)
    Description = models.TextField()
    Creation_date = models.DateTimeField(auto_now=True)
    Deadline_date = models.DateTimeField(null=True)
    Status = models.CharField(max_length=1, choices=TASK_STATUS_CHOICES, default=STATUS_NEW)

    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'

    def __str__(self):
        return self.Title
