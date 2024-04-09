from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def sign_up(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect(form)
        else:
            form = SignupForm()
        response = {'form': form}
        return render(request, 'sign_up_form.html', response)
    except Exception as e:
        print(e)
        return HttpResponse("Error!\nSomething went wrong")


def login_process(request):
    try:
        response = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                page_return = request.POST.get('page_return', '/main')
                return redirect(page_return)
            else:
                response = {'error': 'Username or Password is incorrect'}
                messages.success(request, "Error")
                return render(request, 'login.html', response)
        else:
            if request.user.is_authenticated:
                response['page_return'] = request.GET.get('page_return', '')
                return render(request, 'login.html', response)
            else:
                return redirect('/main')
    except Exception as e:
        print(e)
        return HttpResponse("Error!\nSomething went wrong")




def change_user_paasword(request):
    try:
        response = {}
        if request.method == 'POST':
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            if request.user.is_authenticated:
                user = User.objects.get(username__exact=request.user.username)
                if user.check_password(old_password):
                    user.set_password(new_password)
                    user.save()
                    return redirect('/main')
                else:
                    response['error'] = 'Password is incorrect'
                    messages.success(request, "Error")
                    return render(request, 'change_password_form.html', response)
            else:
                return redirect('/login?page_return=/change_password')
        else:
            response['page_return'] = request.GET.get('page_return', '')
            return render(request, 'change_password_form.html', response)
    except Exception as e:
        print(e)
        return HttpResponse('Error!\nSomething went wrong')


