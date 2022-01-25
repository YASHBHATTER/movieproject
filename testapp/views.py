from django.shortcuts import render
from testapp.forms import Movieform
from testapp.models import Movie

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.htm')
def add_movie_view(request):
    form = Movieform(request)
    if request.method == 'POST':
        form = Movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)

    return render(request,'testapp/addmovie.htm',{'form':form})

def list_movie_view(request):
    movies_list = Movie.objects.all()
    return render(request,'testapp/listmovie.htm',{'movies_list':movies_list})