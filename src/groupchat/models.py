from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
	def __str__(self):
		return self.user
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	create_date = models.DateField(auto_now=True)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=100, blank=True)
	models.ImageField(upload_to = '/static/assets/', blank=True)

class Room(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=1000)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	create_date = models.DateField(auto_now=True)

class RoomGroup(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=1000)
	create_date = models.DateField(auto_now=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=20000, blank=True)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

class RoomMessage(models.Model):
	message_time = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=2000, blank=True)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Message(models.Model):
	message_time = models.DateTimeField(auto_now=True)
	content = models.TextField(max_length=2000, blank=True)
	message_id = models.TextField(max_length=2000, blank=True)