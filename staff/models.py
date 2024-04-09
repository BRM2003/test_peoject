from django.db import models
from django.contrib.auth.models import User
from projects.models import Projects


class Positions(models.Model):
    Title = models.CharField(max_length=256, unique=True),
    Description = models.TextField()
    cr_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='position_cr_by')
    up_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='position_up_by')
    cr_on = models.DateTimeField(auto_now_add=True)
    up_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.Title


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', verbose_name='User')
    Projects = models.ManyToManyField(Projects, null=True, blank=True)
    Position = models.ForeignKey(Positions, on_delete=models.PROTECT, related_name='positions')
    photo = models.ImageField(upload_to='staff', null=True, blank=True)
    update_password = models.BooleanField(default=False)
    cr_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='staff_cr_by')
    up_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='staff_up_by')
    cr_on = models.DateTimeField(auto_now_add=True)
    up_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Staff'
        verbose_name = 'Staff'

    def __str__(self):
        return self.user.username



