from django import forms
from .models import Reply
from .models import Request

class PostForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('title', 'name_of_inhabitant', 'name_of_organisation', 'result')
        model = Request
        fields = ('title', 'name_of_inhabitant', 'phone_number', 'email', 'reason')
