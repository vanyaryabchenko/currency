from django import forms

from currency.models import Source, Rate, ContactUs


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'image'
        )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency',
            'buy',
            'sell',
            'source'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message'
        )
