# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Hours, NotesDjango, NotesFlask,NotesGL,NotesNew,NotesPygame,NotesPyqt5
from .forms import CreateNewList, NotesFormDjango, NotesFormFlask, NotesFormGL, NotesFormNew, NotesFormPygame, NotesFormPyqt5
import random
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

        if len(txt) > 2:
            ls.item_set.create(text=txt, complete=False)
        else:
            print("invalid")

    return render(response, "main/list.html", {"ls": ls})

def home(response): 
    modul = "None"
    hour_data = Hours.objects.get(id=1)
    hour = 0
    text_hour = 0 
    modul_list = ['Django', 'Flask', 'Pygame', 'Git/Linux', 'PyQt5', 'Something new']
    hours_list = [1,2,3,4,5]
    moduls_housr= ['D_h', 'F_h', 'P_h', 'GL_h', 'PQ_h', 'SN_h']
    data_list = ['Django_hour', 'Flusk_hour', 'Pygame_hour', 'Git_Linux_hour', 'PyQt5_hour', 'Some_new_hour']
    if response.method == "GET":
        if response.GET.get('generate_button') == 'generate_button':
            modul = random.choice(modul_list)
            hour = random.choice(hours_list)
            id = modul_list.index(modul)
            if data_list[id] == 'Django_hour': hour_data.Django_hour += int(hour)
            elif data_list[id] == 'Flusk_hour': hour_data.Flusk_hour += int(hour)
            elif data_list[id] == 'Pygame_hour': hour_data.Pygame_hour += int(hour)
            elif data_list[id] == 'Git_Linux_hour': hour_data.Git_Linux_hour += int(hour)
            elif data_list[id] == 'PyQt5_hour': hour_data.PyQt5_hour += int(hour)
            elif data_list[id] == 'Some_new_hour': hour_data.Some_new_hour += int(hour)
            hour_data.save()
    context = {
        'object': hour_data,
        'modul': modul,
        'hour': hour,
    }
        
        
    return render(response, "main/home.html", context)

def create(response):

    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()


        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})

def django(request):
    queryset = NotesDjango.objects.all() 
    form = NotesFormDjango(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormDjango()
    
    context = {
        'form': form,
        'object_list': queryset,
    }
      
    return render(request, 'main/django.html', context)

def flask(request):
    queryset = NotesFlask.objects.all() 
    form = NotesFormFlask(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormFlask()
    
    context = {
        'form': form,
        'object_list': queryset,
    }

    return render(request, 'main/flask.html', context)

def pygame(request):
    queryset = NotesPygame.objects.all() 
    form = NotesFormPygame(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormPygame()
    
    context = {
        'form': form,
        'object_list': queryset,
    }

    return render(request, 'main/pygame.html', context)

def git_Linux(request):
    queryset = NotesGL.objects.all() 
    form = NotesFormGL(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormGL()
    
    context = {
        'form': form,
        'object_list': queryset,
    }

    return render(request, 'main/linux_git.html', context)

def pyQt5(request):
    queryset = NotesPyqt5.objects.all() 
    form = NotesFormPyqt5(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormPyqt5()
    
    context = {
        'form': form,
        'object_list': queryset,
    }

    return render(request, 'main/pyqt5.html', context)

def something_new(request):
    queryset = NotesNew.objects.all() 
    form = NotesFormNew(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesFormNew()
    
    context = {
        'form': form,
        'object_list': queryset,
    }

    return render(request, 'main/some_new.html', context)