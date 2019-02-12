import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

'''Reference

MDN: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

- What kind of options for each field?


'''

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        # go through the default validators and converted into Python datetime.datetime object
        data = self.cleaned_data['renewal_date'] 
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past')) # using _(), good practice if you want to translate your site later.

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data