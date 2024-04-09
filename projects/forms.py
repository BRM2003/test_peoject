from django.forms import ModelForm, TextInput, Textarea, Select, DateInput, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *


class AddProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['Title', 'Description', 'End_date', 'Status']

        widgets = {
            "Title": TextInput(attrs={
                'name': "pr_name",
                'class': "form-filter",
                'placeholder': "Title"
            }),
            "Status": Select(attrs={
                'name': "pr_status",
                'class': "form-filter",
                'placeholder': "Status"
            }),
            "Description": Textarea(attrs={
               'name': 'pr_description',
               'class': 'form-filter',
               'placeholder': 'Description'
            }),
            "Start_date": DateInput(attrs={
                'name': "pr_start_date",
                'class': "form-filter",
                'placeholder': "Start date"
            }),
            "End_date": SelectDateWidget(attrs={
                'name': "pr_end_date",
                'class': "form-filter",
                'placeholder': "End date"
            }),
        }
