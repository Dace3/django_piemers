from django.db import models


class Room(models.Model):
    description = models.CharField(max_length=125)

    def __str__(self):
        return f'{self.pk} [{self.description}]'


class Visit(models.Model):

    name = models.CharField(max_length=125)
    date = models.DateField()
    reason = models.CharField(max_length=125)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
