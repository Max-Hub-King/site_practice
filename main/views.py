# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Hours, Notes
from .forms import CreateNewList
import random
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
    hour = 0
    text_hour = 0 
    modul_list = ['Django', 'Flask', 'Pygame', 'Git/Linux', 'PyQt5', 'Something new']
    hours_list = [1,2,3,4,5]
    moduls_housr= ['D_h', 'F_h', 'P_h', 'GL_h', 'PQ_h', 'SN_h']
    data_list = ['Django_hour', 'Flusk_hour', 'Pygame_hour', 'GIT_Linux_hour', 'PyQt5_hour', 'Some_new_hour']
    if response.method == "GET":
        if response.GET.get('generate_button') == 'generate_button':
            modul = random.choice(modul_list)
            hour = random.choice(hours_list)
            id = modul_list.index(modul)
            text_hour = moduls_housr[id]
        
        
    return render(response, "main/home.html", {'modul': modul, 'hour': hour, str(text_hour): hour})

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

def django(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')


    
    return render(response, 'main/django.html', {'note': note})

def flask(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')

    return render(response, 'main/flask.html', {'note': note})

def pygame(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')

    return render(response, 'main/pygame.html', {'note': note})

def git_Linux(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')

    return render(response, 'main/linux_git.html', {'note': note})

def pyQt5(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')

    return render(response, 'main/pyqt5.html', {'note': note})

def something_new(response):
    note = ''
    if response.method == "POST":
        if response.POST.get('D_button') == 'D_button':
            note = response.POST.get('note_text')

    return render(response, 'main/some_new.html', {'note': note})