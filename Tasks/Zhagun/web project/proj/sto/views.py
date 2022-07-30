from django.shortcuts import  render
from .forms import AddModelFormRecord


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request,'contacts.html')

def add_model_form_record(request):
    if request.method == 'POST':
        form = AddModelFormRecord(request.POST)
        if form .is_valid():
            form.save()
            return render(request,'answer.html')
        
    else:
        form=AddModelFormRecord()
        return render(request,'record.html',{'form':form})










