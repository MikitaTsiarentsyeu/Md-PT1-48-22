from django.shortcuts import redirect, render
from forum.models import Books
from forum.models import Theme
from forum.models import Information
from datetime import datetime
from .forms import AddTheme, AddInformation


def home(request):
    return render(request, 'home.html')

def books(request):
    all_books = Books.objects.all()
    series = []
    for b in all_books:
        if b.series not in series:
            series.append(b.series)
    return render(request, 'books.html', {'books':all_books, 'series':series})#'series':all_series, })

def themas(request):
    all_themas = Theme.objects.all().order_by('-create')
    return render(request, 'themas.html', {'themas':all_themas})

def inform(request, theme_title):
    request.session['theme_title'] = theme_title
    theme = Theme.objects.get(title=theme_title)
    inform = theme.information_set.all()
    return render(request, 'inform.html', {'inform':inform, 'theme_title':theme_title})#, 'theme_id':theme_id})

def informs(request):
    theme_name = request.session.get('theme_name')
    theme_title = Theme.objects.get(title=theme_name)
    return inform(request, theme_title)

def add_theme(request):
    if request.method == 'POST':
        current_time = datetime.now()
        form = AddTheme(request.POST,request.FILES)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.create = current_time
            theme.create = datetime.now()
            theme.save()
            form.save_m2m()
            return redirect('themas')
    else:
        form = AddTheme()    
    return render(request,'add_theme.html', {'form':form})

def add_information(request):
    if request.method == 'POST':      
        theme_title = request.session.get('theme_title')
        theme_name = Theme.objects.get(title=theme_title)
        current_time = datetime.now()
        form = AddInformation(request.POST,request.FILES)
        if form.is_valid():
            inform = form.save(commit=False)
            inform.create = current_time
            inform.theme = theme_name
            inform.author = request.user.username
            inform.save()
            form.save_m2m()
            return redirect('themas')
    else:
        form = AddInformation()    
    return render(request,'add_informations.html', {'form':form})