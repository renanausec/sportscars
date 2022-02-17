from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contato.models import Contato
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você está logado!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Dados incorretos!')
            return redirect('login')
    return render(request, 'accounts/login.html')

def cadastro(request): 
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já cadastrado!')
                return redirect('cadastro')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail já cadastrado!')
                    return redirect('cadastro')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Você está logado!')
                    user.save()
                    return redirect('dashboard')

        else:
            messages.error(request, 'As senhas são distintas!')
            return redirect('cadastro')

    else:
        return render(request, 'accounts/cadastro.html')

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contato.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')

    return redirect('home')