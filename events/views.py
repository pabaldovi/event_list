from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Event
from .forms import EventForm

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'events/index.html'
    model = Event

    def get_queryset(self):
        """Return all events created by current user in ascending order."""
        return Event.objects.filter(author=self.request.user).order_by('date')

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    login_url = '/login/'
    template_name = 'events/create.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    template_name = 'events/detail.html'
    model = Event

    def get_queryset(self):
        """Return event created by current user."""
        return Event.objects.filter(author=self.request.user)

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

class DescendingView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'events/index.html'
    model = Event

    def get_queryset(self):
        """Return all events created by current user in descending order."""
        return Event.objects.filter(author=self.request.user).order_by('-date')

class DescriptionSearchView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'events/index.html'
    model = Event

    def get_queryset(self):
        """Return events created by current user that contains the query in ascending order."""
        query = self.request.GET.get('q')
        if query:
            object_list = (Event.objects
                            .filter(author=self.request.user)
                            .filter(description__icontains=query)
                            .order_by('date'))
        else:
            object_list = Event.objects.none()
        return object_list

def ChartView(request):
    jan_events_count = Event.objects.filter(author=request.user).filter(date__month='1').count()
    feb_events_count = Event.objects.filter(author=request.user).filter(date__month='2').count()
    mar_events_count = Event.objects.filter(author=request.user).filter(date__month='3').count()
    apr_events_count = Event.objects.filter(author=request.user).filter(date__month='4').count()
    may_events_count = Event.objects.filter(author=request.user).filter(date__month='5').count()
    jun_events_count = Event.objects.filter(author=request.user).filter(date__month='6').count()
    jul_events_count = Event.objects.filter(author=request.user).filter(date__month='7').count()
    aug_events_count = Event.objects.filter(author=request.user).filter(date__month='8').count()
    sep_events_count = Event.objects.filter(author=request.user).filter(date__month='9').count()
    oct_events_count = Event.objects.filter(author=request.user).filter(date__month='10').count()
    nov_events_count = Event.objects.filter(author=request.user).filter(date__month='11').count()
    dec_events_count = Event.objects.filter(author=request.user).filter(date__month='12').count()

    events_per_month = [
        jan_events_count,
        feb_events_count,
        mar_events_count,
        apr_events_count,
        may_events_count,
        jun_events_count,
        jul_events_count,
        aug_events_count,
        sep_events_count,
        oct_events_count,
        nov_events_count,
        dec_events_count
    ]

    context = {'events_per_month': events_per_month}
    return render(request, 'events/chart.html', context)
