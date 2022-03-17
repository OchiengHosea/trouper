from webbrowser import get
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from accounts.forms import LoginForm
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context
    
    def post(self, *args, **kwargs):
        data = self.request.POST
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user:
            auth_login(self.request, user)
            return redirect(reverse('base:home'))
        context = self.get_context_data()
        context["form"] = LoginForm(self.request.POST)
        context['errors'] = 'No user with specified credentials'
        return render(self.request, self.template_name, context)