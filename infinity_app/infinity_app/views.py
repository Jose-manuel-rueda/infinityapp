
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'infinity_app/home.html', {'user': request.user})

def about(request):
    return render(request, 'infinity_app/about.html')

def contact(request):
    return render(request, 'infinity_app/contact.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'infinity_app/signup.html', {'form': form})
@login_required  # Requiere que el usuario esté autenticado
def perfil(request):
    return render(request, 'infinity_app/perfil.html', {'user': request.user})