from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MyModel
# Create your views here.

def home(request):
    model=MyModel.objects.all()
    template= loader.get_template('home.html')
    context={
        'model':model
    }

    return HttpResponse(template.render(context,request))