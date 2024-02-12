from django import forms

class UpdateTask(forms.Form):
    title = forms.CharField(max_length=255)
