from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from course_app.models import Track
from .forms import TraineeForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def trainee_list(request):
    trainees = Trainee.objects.select_related('track')  
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("trainee_list")
    else:
        form = TraineeForm()
    
    return render(request, "trainee/add_trainee.html", {"form": form})

def update_trainee(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("trainee_list")
    else:
        form = TraineeForm(instance=trainee)
    
    return render(request, "trainee/update_trainee.html", {"form": form})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')
