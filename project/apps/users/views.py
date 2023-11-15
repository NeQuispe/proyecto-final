from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms
from django.contrib import messages

# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.user.is_staff:
            form = forms.UserStaffCreationForm(request.POST)
        else:
            form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, "Usuario creado correctamente.", extra_tags="alert alert-success")
            return redirect('home:index')
    else:
        if request.user.is_staff:
            form = forms.UserStaffCreationForm()
        else:
            form = forms.CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})