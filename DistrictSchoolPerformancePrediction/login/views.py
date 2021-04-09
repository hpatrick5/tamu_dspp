from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'title': 'DSPP'
    }
    return render(request, 'login/home.html', context)


def about(request):
    return render(request, 'login/about.html')


def handle_uploaded_file(f):
    with open('random_name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('/success/url/')
            return render(request, 'login/home.html')
    else:
        form = UploadFileForm()
    return render(request, 'login/upload.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now Login')
            return redirect('main-login')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form': form})
