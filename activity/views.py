from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Activity
from .forms import ActivityForm


def activity(request):
     if request.method == "POST":
         form = ActivityForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.save()
             messages.success(request, 'Atividade cadastrada com sucesso!')
             return redirect('index')
     else:
         form = ActivityForm()
     return render(request, 'activity/index.html', {'form':form})
