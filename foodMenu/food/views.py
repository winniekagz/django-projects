from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from django.template import loader

# Create your views here.
def hello_word(request):
    food_list=Food.objects.all()
    template=loader.get_template('index.html')
    context={
        'food_list':food_list,
    }
    return HttpResponse(template.render(context,request))
