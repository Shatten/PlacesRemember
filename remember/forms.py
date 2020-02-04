from django import forms
from .models import Remember


class RememberForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Remember
        fields = ('title', 'description', 'map_coordinates')
