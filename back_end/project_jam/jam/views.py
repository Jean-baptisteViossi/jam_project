from django.shortcuts import render, redirect
from .models import Histoire
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import HistoirePartagee
from .models import Mission
from .forms import MissionForm

def accueil(request):
    histoires = Histoire.objects.all()
    return render(request, 'accueil.html', {'histoires': histoires})

def contact(request):
    return render(request, 'contact.html')

def partager(request):
    if request.method == 'POST':
        titre = request.POST.get('titre', '')
        contenu = request.POST.get('contenu', '')
        histoire = Histoire(titre=titre, contenu=contenu)
        histoire.save()
        return HttpResponseRedirect(reverse('accueil'))
    return render(request, 'partager.html')


def partager_histoire(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        contenu = request.POST.get('contenu')
        histoire = HistoirePartagee.objects.create(titre=titre, contenu=contenu)
        histoires = HistoirePartagee.objects.all()
        return render(request, 'partager.html', {'histoires': histoires})
    else:
        histoires = HistoirePartagee.objects.all()
        return render(request, 'partager.html', {'histoires': histoires})


def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'missions/mission_list.html', {'missions': missions})

def mission_detail(request, pk):
    mission = Mission.objects.get(pk=pk)
    return render(request, 'missions/mission_detail.html', {'mission': mission})

def mission_new(request):
    if request.method == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save()
            return redirect('mission_detail', pk=mission.pk)
    else:
        form = MissionForm()
    return render(request, 'missions/mission_edit.html', {'form': form})

def mission_edit(request, pk):
    mission = Mission.objects.get(pk=pk)
    if request.method == "POST":
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            mission = form.save()
            return redirect('mission_detail', pk=mission.pk)
    else:
        form = MissionForm(instance=mission)
    return render(request, 'missions/mission_edit.html', {'form': form})

def mission_delete(request, pk):
    mission = Mission.objects.get(pk=pk)
    mission.delete()
    return redirect('mission_list')


