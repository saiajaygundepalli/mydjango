from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import CustomRegistrationFrom
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =="POST":
        register_form = CustomRegistrationFrom(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('New User Created'))
            return redirect('register')
    else:
        register_form = CustomRegistrationFrom
    return render(request, 'register.html', {'register_form' : register_form})