from django import forms

class search_form(forms.Form):
    input = forms.CharField()