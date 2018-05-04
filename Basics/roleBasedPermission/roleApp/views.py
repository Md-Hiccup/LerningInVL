from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.http import HttpResponse
from django.views import View
# Create your views here.
from .forms import SignUpForm

class Signup(View):
    def get(self, request):
        return render(request, "roleApp/signup.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'roleApp/signup.html', {'form': form})