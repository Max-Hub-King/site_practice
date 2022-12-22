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


class NotesDjango(models.Model):
	data_django = models.CharField(max_length=10000)

class NotesFlask(models.Model):
	data_flask = models.CharField(max_length=10000)

class NotesPygame(models.Model):
	data_pygame = models.CharField(max_length=10000)

class NotesGL(models.Model):
	data_git_linux = models.CharField(max_length=10000)

class NotesPyqt5(models.Model):
	data_pyqt5 = models.CharField(max_length=10000)

class NotesNew(models.Model):
	data_new = models.CharField(max_length=10000)

