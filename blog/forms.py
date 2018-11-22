from django import forms
from .models import Reply
from .models import Request

class PostForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('title', 'name_of_inhabitant', 'name_of_organisation', 'result')
        model = Request
        fields = ('title1', 'name_of_inhabitant1', 'phone_number', 'email', 'reason')
