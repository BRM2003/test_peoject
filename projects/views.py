from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def main(request):
    try:
        response = {}
        if request.method == 'GET':
            if request.user.is_authenticated:
                response = {
                    'is_superuser': request.user.is_superuser
                }
            else:
                return redirect('/login?page_return=/main/')
        else:
            if request.user.is_authenticated:
                response = {
                    'is_superuser': request.user.is_superuser
                }
        return render(request, 'main/projects.html', response)
    except Exception as e:
        print(e)
        return HttpResponse("Error!\nSomething went wrong")


def add_project(request):
    try:
        if request.method == 'GET':
            if request.user.is_authenticated:
                add_proj_form = AddProjectsForm()
                response = {
                    'add_proj_form': add_proj_form,
                    'is_superuser': request.user.is_superuser
                }
                return render(request, 'main/add_project_form.html', response)
            else:
                redirect('/login?page_return=/main/add_project')
        else:
            if request.user.is_authenticated:
                response = {'is_superuser': request.user.is_superuser}
                add_proj_form = AddProjectsForm(request.POST)
                if add_proj_form.is_valid():
                    add_proj_form.save()
                    redirect('/main')
            return render(request, 'main/projects.html', response)
    except Exception as e:
        print(e)
        return HttpResponse("Error!\nSomething went wrong")
