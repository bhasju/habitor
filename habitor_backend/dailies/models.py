from django.db import models
from django.contrib.auth.models import User

class task(models.Model):
	title = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	points = models.PositiveSmallIntegerField(choices = [(0,'TRIVIAL'),(1,'BASIC'),(2,'EASY'),(3,'MEDIUM'),(5,'HARD'),(8,'TROLL')], default=2)
	
class subtask(models.Model):
	title = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	parent = models.ForeignKey(task, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	points = models.PositiveSmallIntegerField(choices = [(0,'TRIVIAL'),(1,'BASIC'),(2,'EASY'),(3,'MEDIUM'),(5,'HARD'),(8,'TROLL')], default=1)