from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meeting_title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=255)
    meeting_agenda = models.TextField()

    def __str__(self):
        return self.meeting_title

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'

class MeetingMinutes(models.Model):
    minutes_text = models.TextField()
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)

    def __str__(self):
        return self.minutes_text

    class Meta:
        db_table = 'meeting_minutes'
        verbose_name_plural = 'meeting_minutes'

class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    date_entered = models.DateField()
    resource_url = models.URLField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resource_description = models.TextField()

    def __str__(self):
        return self.resource_name

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'

class Event(models.Model):
    event_title = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.event_title

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
