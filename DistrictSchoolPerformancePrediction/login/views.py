from django.shortcuts import render, redirect
from .forms import UserRegisterForm
    #to do file upload - incomplete
    ##
    #
from .forms import Profile_Form
from django.contrib.auth.models import User

##end of file upload

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    #commented out context as it added DSPP twice in title
    #context = {
     #   'title': 'DSPP'
    #}
    #return render(request, 'login/home.html', context)
    return render(request, 'login/home.html')

def about(request):
    return render(request, 'login/about.html')


#def handle_uploaded_file(f):
#    with open('random_name.txt', 'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)

#accepted file types for upload
IMAGE_FILE_TYPES = ['csv']

@login_required
#def upload_file(request):
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            handle_uploaded_file(request.FILES['file'])
#            # return HttpResponseRedirect('/success/url/')
#            return render(request, 'login/home.html')
#    else:
#        form = UploadFileForm()
#    return render(request, 'login/upload.html', {'form': form})


def upload_file(request):

    username = request.user.username
    initial_data = {
        'fname' : username,
        'grade' :5
    }
    form = Profile_Form(initial=initial_data, instance = User)
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'file_upload/error.html')
            user_pr.save()
            return render(request, 'file_upload/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'login/upload.html', context)


#def upload_file(request):
    #corresponding form name
 #   form = UploadFileForm()
 #   if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            user_pr = form.save(commit=False)
 #           user_pr.display_picture = request.FILES['display_picture']
#            file_type = user_pr.display_picture.url.split('.')[-1]
 #           file_type = file_type.lower()
 #           if file_type not in IMAGE_FILE_TYPES:
#                return render(request, 'login/error.html')
#            user_pr.save()
#            return render(request, 'login/details.html', {'user_pr': user_pr})
#    context = {"form": form,}
#    return render(request, 'login/create.html', context)




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been created! You can now Login')
            return redirect('main-login')
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
			messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"form":form})
