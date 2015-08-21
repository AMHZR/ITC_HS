__author__ = 'aamir'
from django import forms

from ajax_select.fields import AutoCompleteSelectField
from models import Section


class Search(forms.Form):
    pass


class ITC_HSForm(forms.Form):
    ITC_hs4 = AutoCompleteSelectField('hs4', required=True, help_text='', label='Category')


STATUS_CHOICES = [('', 'Select Section')]
STATUS_CHOICES.extend([(obj.name, obj.name) for obj in Section.objects.all()])


class SearchForm(forms.Form):
    section = forms.ChoiceField(choices=STATUS_CHOICES, label="Section", initial='', widget=forms.Select(attrs={'class':'form-control'}),
                                required=True)

    chapter = forms.ChoiceField(choices=[], label="Chapter", initial='', widget=forms.Select(attrs={'class':'form-control'}),
                                required=False)

    article = forms.ChoiceField(choices=[], label="Article", initial='', widget=forms.Select(attrs={'class':'form-control'}),
                                required=False)

    keywords = forms.CharField(required=False, label='Keywords',
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search for HS Codes'}))