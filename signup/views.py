from django.shortcuts import render, redirect
from .models import Signup

def success_page(request):
    variables = {
        'accounts':Signup.objects.all(),
    }
    return render(request, 'view.html' ,variables)

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        account_type = request.POST.get('account-type')
        signup = Signup(username=username, email=email, password=password, account_type=account_type)
        signup.save()
        return redirect('vio')

    variables = {
        'title': 'Signup',
    }
    return render(request, 'sgnup.html', variables)
