from django.shortcuts import render, redirect
from .forms import rainbow_6form
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request, 'reporter/Homepage.html')

def get_details(username):
    pass

def Rainbow_handler(request):
    if request.method == 'POST':
            form = rainbow_6form(data=request.POST)
            if form.is_valid():
                details=get_details(form.cleaned_data['username'])
                print(form.cleaned_data['username'])
                print(form.cleaned_data['smurf'])
                return redirect(reverse('home'))
            else:
                return redirect(reverse('Rainbow'))

    elif request.method=='GET':
        form = rainbow_6form()
        args = {'form': form}
        return render(request, 'reporter/Rainbow_form.html', args)