from django.shortcuts import render
from .models import Opinion, Tasks

# Create your views here.

def main_page(request):
    tasks = Tasks.objects.all()
    opinion1 = Opinion.objects.all()[0]
    opinion2 = Opinion.objects.all()[1]
    context = {'tasks':tasks,
               'opinion1':opinion1,
               'opinion2':opinion2,
                
                }

    return render(request, template_name='index.html', context=context)

def gallery_page(request):
    images = Tasks.objects.all()

    context = {'images':images}

    return render(request, template_name='gallery.html', context=context)    
