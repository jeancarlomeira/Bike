from django import forms
from .models import AnualObjective

class AnualObjectiveForm(forms.ModelForm):
    class Meta:
        model = AnualObjective
        fields = ('objective',)
