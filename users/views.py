from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Display a blank registration form
        form = UserCreationForm
    else:
        # process the complete form
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect ('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)    
