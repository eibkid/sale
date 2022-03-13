from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExtractForm



    

def extract_detail(request):

    if request.method == 'POST':
        form = ExtractForm(request.POST)
        if form.is_valid():
            form.save()


    form = ExtractForm()
    return render(request, 'form.html', {'form': form})

