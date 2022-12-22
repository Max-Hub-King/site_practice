from django.contrib import admin
from .models import ToDoList, Item, Hours, NotesDjango, NotesFlask,NotesGL,NotesNew,NotesPygame,NotesPyqt5
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(NotesDjango)
admin.site.register(NotesFlask)
admin.site.register(NotesGL)
admin.site.register(NotesNew)
admin.site.register(NotesPygame)
admin.site.register(NotesPyqt5)
admin.site.register(Hours)
