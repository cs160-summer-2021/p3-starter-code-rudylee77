from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def homepage(request):
    return render(request, 'coloring/homepage.html')
def search(request):
    return render(request, 'coloring/search.html')
def coloringpage(request):
    return render(request, 'coloring/coloringpage.html')
def new(request):
    return render(request, 'coloring/new.html')
def animals(request):
    return render(request, 'coloring/animals.html')