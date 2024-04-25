from django.shortcuts import render, redirect 
from .models import *
from .forms import StudentsForm

# Create your views here.
def index(request):
    form = StudentsForm()
    students = Students.objects.all()
    template = 'main/index.html'
    context = {'students':students}

    if request.method == 'POST':
        if 'deleteStudent' in request.POST:
            pk = request.POST.get('deleteStudent')
            students = Students.objects.get(id=pk)
            students.delete()
        elif 'editStudent' in request.POST:
            pk = request.POST.get('editStudent')
            students = Students.objects.get(id=pk)
            form = StudentsForm(instance=students)
            print(form)
    return render(request, template, context)

# # Create your views here.
def add(request):
    form = StudentsForm()

    template = 'main/add/add.html'
    if request.method == 'POST':
        if 'addStudent' in request.POST:
            form = StudentsForm(request.POST)
            form.save()
    context = {}
    return render(request, template, context)

def update(request, pk):
    students = Students.objects.get(id=pk)

    form = StudentsForm(instance=students)

    template = 'main/update/update.html'
    if request.method == "POST":
        if 'updateStudents' in request.POST:
            form = StudentsForm(request.POST, instance=students)
            form.save()
            
            return redirect('/')
    context = {'form':form}
    return render(request, template, context)