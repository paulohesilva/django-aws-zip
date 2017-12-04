from django.db import models


class Task(models.Model):

    STATUS_CHOICES = (
        (0, 'in progress'),
        (1, 'done'),
        (2, 'fail'),
    )

    description = models.CharField(null=True, blank=True, max_length=100)
    key = models.CharField(null=True, blank=True, max_length=100)
    num_file = models.IntegerField(null=True, blank=True)
    percent = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

