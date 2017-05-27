from django import forms
from django.forms import ModelForm
from .models import Room


# noinspection PyPep8,PyPep8
class CourseForm(forms.Form):
    course = forms.CharField(label='Course Name', max_length=100)
    num_lectures = forms.IntegerField(label='Number of Lectures')


# noinspection PyPep8
class RoomForm(ModelForm):
    # noinspection PyPep8,PyPep8,PyPep8
    class Meta:
        model = Room
        # noinspection PyPep8
        exclude = ['title']
