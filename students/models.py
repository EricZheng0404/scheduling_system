from django.db import models

from datetime import date, datetime, timedelta

# Create your models here.

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

class Student(models.Model):
    name = models.CharField(max_length=64)
    time = models.TimeField(blank=False) # start_time
    day = models.IntegerField(choices=DAYS_OF_WEEK) # student's available days of week

    def __str__(self):
        return f"{self.name}, {self.day}, {self.time}"

class Teacher(models.Model):
    name = models.CharField(max_length=64)
    start_time = models.TimeField(blank=False) # the start time of the available period of a teacher
    end_time = models.TimeField(blank=False) # the end time of the available period of a teacher
    day = models.IntegerField(choices=DAYS_OF_WEEK) # teacher's available day of a week

    def __str__(self):
        return f"{self.name}, {self.day}: {self.start_time} to {self.end_time}"

    def minutes_slices(self, minutes=15):
        # We can't add minutes to datetime.time, so we need to convert it to datetime
        start_date_time = datetime.combine(date.today(), self.start_time)
        end_date_time = datetime.combine(date.today(), self.end_time)
        next_time = start_date_time
        minutes_slices = [next_time.time()]
        if start_date_time < end_date_time:
            while next_time < end_date_time:
                next_time += timedelta(minutes=minutes)
                minutes_slices.append(next_time.time())
        return minutes_slices