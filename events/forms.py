from django import forms
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description', 'date']
        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs = {
            'class': 'form-control mb-3',
            'placeholder': 'description',
        }
        self.fields['date'].widget.attrs = {
            'class': 'form-control mb-3',
        }