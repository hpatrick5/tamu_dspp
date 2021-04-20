from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm


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
            user = form.save()
            auth_login(request, user)
            messages.success(
                request, f'Your account has been created! You can now Login')
            return redirect('login-home')
    else:
        form = UserRegisterForm()
    return render(request, 'login/register.html', {'form': form})

def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('login-home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"form":form})