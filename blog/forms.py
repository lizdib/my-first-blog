from django import forms
from .models import Reply
from .models import Request
from .models import Reply_register
from .models import Request_register

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('id', 'name_of_inhabitant', 'result')

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('id', 'name_of_inhabitant', 'phone_number', 'email', 'reason')

class Reply_registerForm(forms.ModelForm):
    class Meta:
        model = Reply_register
        fields = ('title', 'reply_number', 'name_of_inhabitant', 'result', 'name_of_doer', 'request_status', 'created_date')

class Request_registerForm(forms.ModelForm):
    class Meta:
        model = Request_register
        fields = ('title', 'request_number', 'name_of_inhabitant', 'phone_number', 'email', 'reason', 'name_of_doer', 'request_status', 'created_date')
