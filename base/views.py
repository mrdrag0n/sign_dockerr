from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Profile


# Create your views here.


# Authentication Views
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profiles')


class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('profiles')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


# Functionality views
class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'base/cert_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = context['profiles'].filter(user=self.request.user)
        return context


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profil'
    template_name = 'base/cert_detail.html'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['common_name', 'organization', 'organization_unit_name', 'locality', 'state_name', 'country_name',
              'email']
    template_name = 'base/cert_form.html'
    success_url = reverse_lazy('profiles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['common_name', 'organization', 'organization_unit_name', 'locality', 'state_name', 'country_name',
              'email']
    template_name = 'base/cert_update.html'
    success_url = reverse_lazy('profiles')


class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    context_object_name = 'profil'
    success_url = reverse_lazy('profiles')
    template_name = 'base/confirm_cert_delete.html'

# Certificate Sign Sde
