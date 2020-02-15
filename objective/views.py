from django.shortcuts import render, redirect
from django.contrib import messages

from .models import AnualObjective
from .forms import AnualObjectiveForm


def objective(request):
     if request.method == "POST":
         form = AnualObjectiveForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             obj = AnualObjective.objects.get(slug='1')
             obj.delete()
             post.save()
             messages.success(request, 'Novo objetivo cadastrado com sucesso!')
             return redirect('index')
     else:
         form = AnualObjectiveForm()
     return render(request, 'objective/index.html', {'form':form})
