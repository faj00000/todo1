from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks':tasks , 'form':form}
    return render(request,'tasks/list.html',context=context)


def updateTask(request,pk):
    task =Task.objects.get(id=pk)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form,'x':pk}
    return render(request, 'tasks/update_task.html',context=context)

def delete(request,pk):
    task =Task.objects.get(id=pk)
    if request.method == 'POST':
        print(str(pk)+'-----------------------------deleted----')
        task.delete()
        return redirect('/')
    context = {'form': task}
    return render(request, 'tasks/delete.html',context=context)