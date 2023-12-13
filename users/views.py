from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .forms import LoginForm, RegisterForm, UserForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method != 'POST':
        # if the request is not a post request, then show an empty form
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False) # convert the password to a hash value -> for password safety
            new_user.set_password(form.cleaned_data.get('password')) # convert to hash value
            new_user.save() # save to the db
            return HttpResponse('register success!')
    
    context = {'form':form}
    return render(request, 'users/register.html', context)

def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else :
        form = LoginForm(request.POST) # get the data from form
        if form.is_valid(): # check the validity of the form
            username = form.cleaned_data['username'] # the form is a dict, using [] not ()
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('users:user_profile')
            else:
                return HttpResponse('login failed')
            
        
    context = {'form':form}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'users/user_profile.html', {'user': user})

@login_required(login_url='users:login')
def editor_users(request):
    # logic in edit user information
    # define a form first
    user = User.objects.get(id=request.user.id) # get current user
    if request.method == "POST":
        # empty form will be shown if first login -> no profile exist
        try:
            # if user profile exists
            user_profile = user.userprofile
            # edit and save logic:
            form = UserForm(request.POST, instance=user) # instance shows original data
            # user profile and user is one on one relationship
            user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            
            if form.is_valid() and user_profile_form.is_valid():
                form.save()
                user_profile_form.save()
                
                return redirect("users:user_profile")
            
        except UserProfile.DoesNotExist:
            # instead shown an error page, show an empty form
            form = UserForm(request.POST, instance=user)
            user_profile_form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid() and user_profile_form.is_valid():
                form.save()
                # set commit equals to false -> save the data in memory.
                new_user_profile = user_profile_form.save(commit=False)
                new_user_profile.owner = request.user
                new_user_profile.save()
                
                return redirect("users:user_profile")
    else:
        # show the page
        try:
            user_profile = user.userprofile
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm(instance=user_profile)
            
        except UserProfile.DoesNotExist:
            # instead shown an error page, show an empty form
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm()
        
    return render(request, 'users/editor_users.html', locals())