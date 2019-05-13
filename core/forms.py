from django import forms
from .models import Step, Process, ProcessStepConfig

class StepForm(forms.ModelForm):

    class Meta:
        model = Step
        fields = ['name',]

class ProcessForm(forms.ModelForm):

    class Meta:
        model = Process
        fields = ['name',]

class ProcessStepConfigForm(forms.ModelForm):

    class Meta:
        model = ProcessStepConfig
        fields = ['step', 'time', 'order', ]