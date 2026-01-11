from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    TYPE = (
        ('Direct', 'Direct'),
        ('Group', 'Group'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    type = models.TextField('Type', choices=TYPE, default="Direct")
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return str(self.id) + " | " + self.name + " | " + self.type


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        return str(self.id) + " | " + self.room.name + " | " + self.date_added