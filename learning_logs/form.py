from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        Model = Topic
        fields = ['text']
        labels = {'labels': ''}