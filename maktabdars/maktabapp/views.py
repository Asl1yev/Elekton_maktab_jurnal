from django.shortcuts import render, redirect
from .models import Fan,Student,Baholar
from .forms import AddFanForm,AddStudntForm,AddBahoForm

# Create your views here.


def home(request):
    return render(request,'base.html')

def talaba(request):
    name=Student.objects.all()
    context={
        'name':name,

    }
    return render(request,'oquchi_royxat.html',context)

def fan(request):
    name = Fan.objects.all()
    context = {
        'name': name,

    }
    return render(request,'fanlar.html',context)

def baho(request):
    name = Baholar.objects.all()
    context = {
        'name': name,

    }

    return render(request,'baholar.html',context)



# Fan baho talaba qoshish uchun viewlar

def fanadd(request):
    form = AddFanForm()
    if request.method == 'POST':
        form = AddFanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fanlar')
        else:
            form = AddFanForm()

    context = {
        'form': form
    }
    return render(request, 'add/add_fan.html', context)


def bahoadd(request):
    form = AddBahoForm()
    if request.method == 'POST':
        form = AddBahoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baholar')
        else:
            form = AddBahoForm()

    context = {
        'form': form
    }
    return render(request, 'add/add_baho.html', context)


def oquvchiadd(request):
    form = AddStudntForm()
    if request.method == 'POST':
        form = AddStudntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('royxat')
        else:
            form = AddStudntForm()

    context = {
        'form': form
    }
    return render(request, 'add/add_stdent.html', context)









