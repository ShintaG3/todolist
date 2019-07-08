from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def index(request):
    all_items = List.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to the list!'))
            return render(request, "index.html", {"all_items": all_items})
    else:
        return render(request, "index.html", {"all_items": all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('index')

def cross(request, list_id):
    item = List.objects.get(pk=list_id)
    status = item.completed
    if status:
        item.completed = False
        messages.success(request, (f'{item.item} has been uncrossed!'))
    else:
        item.completed = True
        messages.success(request, (f'{item.item} has been completed!'))
    item.save()
    return redirect('index')

def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been updated!'))
            return redirect('index')
    else:
        return render(request, 'edit.html', {"item":item})
