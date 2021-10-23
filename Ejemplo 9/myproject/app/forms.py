from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):

    class Meta:
        model = Survey
        #fields = ["opinion", "isfrendly"]
        fields = '__all__'