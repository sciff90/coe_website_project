#Import Django classes
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#Import the custom models
from opv_costing.models import Material

def index(request):
    return render(request,'opv_costing/index.html')
