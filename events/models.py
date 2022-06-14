from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    def __str__(self):
        return str(self.date_diff) + " days until " + self.description

    @property
    def date_diff(self):
        today = timezone.now()
        return (self.date - today).days + 1

    @property
    def get_date_only(self):
        return self.date.date()