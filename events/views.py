from django.views import generic
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'events/index.html'
    model = Event

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    login_url = '/login/'
    template_name = 'events/create.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:index')

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    template_name = 'events/detail.html'
    model = Event

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    login_url = '/login/'
    template_name = 'events/update.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:index')

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    login_url = '/login/'
    template_name = 'events/delete.html'
    model = Event
    success_url = reverse_lazy('events:index')