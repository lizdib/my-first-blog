from django.contrib import admin
from .models import Reply
from .models import Request
from .models import Reply_register
from .models import Request_register

#admin.site.register(Reply)
#admin.site.register(Request)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_inhabitant', 'name_of_organisation', 'result', 'created_date')

admin.site.register(Reply, ReplyAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_inhabitant', 'phone_number', 'email', 'reason', 'created_date')

admin.site.register(Request, RequestAdmin)

class Reply_registerAdmin(admin.ModelAdmin):
    list_display = ('title', 'reply_number', 'name_of_inhabitant', 'result', 'name_of_doer', 'request_status', 'created_date')

admin.site.register(Reply_register, Reply_registerAdmin)

class Request_registerAdmin(admin.ModelAdmin):
    list_display = ('title', 'request_number', 'name_of_inhabitant', 'phone_number', 'email', 'reason', 'name_of_doer', 'request_status', 'created_date')

admin.site.register(Request_register, Request_registerAdmin)
