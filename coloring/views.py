from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def homepage(request):
    return render(request, 'coloring/homepage.html')
def search(request):
    return render(request, 'coloring/search.html')
def coloringpage(request):
    return render(request, 'coloring/coloringpage.html')