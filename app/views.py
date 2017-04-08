from django.shortcuts import render,redirect
from .models import Notebook

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        notes = request.POST.get('notes')
        notebook = Notebook(title=title, notes=notes)
        notebook.save()
        return redirect('/')
    notes = Notebook.objects()
    return render(request,'index.html', {'context': notes},)
