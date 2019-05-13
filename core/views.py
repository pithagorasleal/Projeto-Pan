from django.shortcuts import render, redirect, get_object_or_404
from .forms import StepForm, ProcessForm, ProcessStepConfigForm
from .models import Step, Process, ProcessStepConfig
from django.http import HttpResponse

def login(request):
    return render(request, "login.html")

def index(request):
    
    context = {
        'title': 'Sabadin - Index',
        'setor': 'Inicio'
    }

    return render(request, "index.html", context)

def step_new(request):

    if request.method == "POST":
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('step_new')
    else:
        form = StepForm()

    context = {
        'form': form,
        'objetos': Step.objects.all(),
        'title': 'Etapa'
    }

    return render(request, 'cadastro.html', context)

def process_new(request):

    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('process_new')
    else:
        form = ProcessForm()

    context = {
        'form': form,
        'objetos': Process.objects.all(),
        'title': 'Processo'
    }

    return render(request, 'cadastro.html', context)


def process_config(request, process_id):

    context = {
        'processo': Process.objects.get(id=process_id),
        'processsteps': ProcessStepConfig.objects.all().filter(process=process_id)
    }
    
    return render(request, 'process_config.html', context)

def process_config_step(request, process_name, processstep_id):

    processo = Process.objects.get(name=process_name)

    instance = get_object_or_404(ProcessStepConfig, id=processstep_id)
    form = ProcessStepConfigForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('process_config', processo.id)

    context = {
        'form': form,
        'processo': processo
    }
    
    return render(request, 'process_config_new.html', context)

def process_config_new(request, process_name):

    processo = Process.objects.get(name=process_name)

    if request.method == 'POST':
        form = ProcessStepConfigForm(request.POST)
        if form.is_valid():
            processform = form.save(commit=False)
            processform.process = processo
            processform.save()
            return redirect('process_config', processo.id)

    else:
        form = ProcessStepConfigForm()

    context = {
        'form': form,
        'processo': processo
    }

    return render(request, 'process_config_new.html', context)

def deleteStepFromConfig(request, process_step_id):
    item = ProcessStepConfig.objects.get(id=process_step_id)
    process = item.process

    item.delete()

    return redirect('process_config', process.id)