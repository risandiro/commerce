from django import forms
from .models import Listing, Bid

import datetime

current_year = datetime.datetime.now().year

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['creator', 'active', 'timestamp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_label, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing_classes + 'form-control').strip()

        self.fields['category'].empty_label = "--Undefined--"
        self.fields['starting_bid'].initial = 0.01
        self.fields['starting_bid'].widget.attrs.update({'min': 0.01, 'max': 999.99})
        self.fields['year'].initial = current_year
        self.fields['year'].widget.attrs.update({'max': current_year, 'min': 1837})


class NewBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
