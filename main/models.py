from django.db import models

# Create your models here.
class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text

class Hours(models.Model):
	Django_hour = models.IntegerField(default=0)
	Flusk_hour = models.IntegerField(default=0)
	Pygame_hour = models.IntegerField(default=0)
	Git_Linux_hour = models.IntegerField(default=0)
	PyQt5_hour = models.IntegerField(default=0)
	Some_new_hour = models.IntegerField(default=0)

	def __str__(self):
		return self.Django_hour, self.Flusk_hour, self.Pygame_hour, self.Git_Linux_hour, self.PyQt5_hour, self.Some_new_hour

class Notes(models.Model):
	data = models.CharField(max_length=10000)

	def __str__(self):
		return self.data