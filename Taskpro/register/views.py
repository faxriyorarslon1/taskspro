from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login 
# Create your views here.

def register_view(request):
    form_r = RegisterForm()
    form_l = LoginForm()
    if request.method == "POST":
        form_r = RegisterForm(request.POST)
        form_l = LoginForm(request.POST)
        print("POSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        if form_r.is_valid():
            form_r.save()
            return redirect('/')
        elif form_l.is_valid():
            
            print("VALIDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            username = form_l.cleaned_data["username"]
            password = form_l.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                
                context = { 'form_r':form_r,
                            'form_l':form_l}

                return render(request, template_name='register.html', context=context)

    
    context = { 'form_r':form_r,
                'form_l':form_l}
    
    return render(request, template_name='register.html', context=context)
