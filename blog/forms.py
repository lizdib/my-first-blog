from django import forms
from .models import Reply
from .models import Request

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('title', 'name_of_inhabitant', 'name_of_organisation', 'result')

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('title1', 'name_of_inhabitant1', 'phone_number', 'email', 'reason')
