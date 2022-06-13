from django.views import generic
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    model = Event

class CreateView(generic.edit.CreateView):
    template_name = 'events/create.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:index')

class DetailView(generic.DetailView):
    template_name = 'events/detail.html'
    model = Event

class UpdateView(generic.edit.UpdateView):
    template_name = 'events/update.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:index')