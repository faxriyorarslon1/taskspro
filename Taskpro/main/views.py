from django.shortcuts import render
from .models import Tasks

# Create your views here.

def main_page(request):
    tasks = Tasks.objects.all()
    context = {'tasks':tasks}

    return render(request, template_name='index.html', context=context)
