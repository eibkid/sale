from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ExtractForm




    

def extract_detail(request):

    if request.method == 'POST':
        form = ExtractForm(request.POST)
        if form.is_valid():
            form.save()
        
            return HttpResponseRedirect('/success/')
        else:
            messages.error(request, 'Error')
    

  
    form = ExtractForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    return render(request, 'success.html')