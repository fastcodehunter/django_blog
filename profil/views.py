from django.shortcuts import render,redirect,get_list_or_404
from profil.forms import FormAuthorizationUser,ModelFormRegistrationsUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.views.generic.edit import FormMixin
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re
from  .models import Profil



def sing_in(request):
    if request.method == 'POST':
        form = FormAuthorizationUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_blog')
            else:
                messages.error(request, "The email or password is incorrect. Please check your credentials.")
    else:
        form = FormAuthorizationUser()
    return render(request, 'singin/login.html', {'form': form})
    





class SignUpView(FormMixin, View):
    form_class = ModelFormRegistrationsUser
    template_name = 'singup/registration.html'
    success_url = 'list_blog'

    def get(self, request):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})
    
    from django.contrib.auth import login

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data['email']
            if not self.is_email_exists(email):
                username = form.cleaned_data['username']
                if not self.is_valid_username(username):
                    messages.add_message(request, messages.ERROR, "The user name must contain only small Latin letters, without spaces and forbidden characters.")
                else:
                    password = form.cleaned_data['password1']
                    if not self.is_valid_password(password):
                        messages.add_message(request, messages.ERROR, "The password must contain at least one Latin letter, one digit and at least 8 characters.")
                    else:
                        user = form.save(commit=False)
                        user.set_password(password)
                        user.save()
                        profil = Profil.objects.create(author=user)
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(request, user)
                        return redirect('list_blog')
            else:
                messages.add_message(request, messages.ERROR, "A user with this email already exists.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in the field '{field}': {error}")
        return render(request, self.template_name, {'form': form})





    def is_email_exists(self, email):
        return User.objects.filter(email=email).exists()
    
    def is_valid_password(self, password):
        return len(password) >= 8 and any(char.isalpha() for char in password) and any(char.isdigit() for char in password)
    
    def is_valid_username(self, username):
        return re.match('^[a-z0-9_]+$', username) is not None





@login_required
def view_profil(request,id_author,name__author):
    user=get_list_or_404(User,id=id_author,username=name__author)
    return render(request,'profil/profil.html',{'username': user})