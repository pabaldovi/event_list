from django.views import generic
from .models import Event

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    model = Event