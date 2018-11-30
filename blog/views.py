from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .forms import ReplyForm
from .forms import RequestForm
from .forms import Reply_registerForm
from .forms import Request_registerForm
from .models import Reply
from .models import Request
from .models import Reply_register
from .models import Request_register

def Request_list(request):
    req = Request.objects.order_by('id')
    return render(request, 'show_requests.html', {'req': req})

def Reply_list(request):
    rep = Reply.objects.order_by('id')
    return render(request, 'show_replies.html', {'rep': rep})

def Request_register_list(request):
    reqreg = Request_register.objects.order_by('title')
    return render(request, 'show_request_register.html', {'reqreg': reqreg})

def Reply_register_list(request):
    repreg = Reply_register.objects.order_by('title')
    return render(request, 'show_reply_register.html', {'repreg': repreg})

def Request_detail(request, pk):
    req = get_object_or_404(Request, pk=pk)
    return render(request, 'blog/Request_detail.html', {'Request': req})

def Reply_detail(request, pk):
    rep = get_object_or_404(Reply, pk=pk)
    return render(request, 'blog/Reply_detail.html', {'Reply': rep})

def Request_register_detail(request, pk):
    reqreg = get_object_or_404(Request_register, pk=pk)
    return render(request, 'blog/Request_register_detail.html', {'Request_register': reqreg})

def Reply_register_detail(request, pk):
    repreg = get_object_or_404(Reply_register, pk=pk)
    return render(request, 'blog/Reply_register_detail.html', {'Reply_register': repreg})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'tit' in request.GET and request.GET['tit'] and 'name' in request.GET and request.GET['name']:
        tit = request.GET['tit']
        name = request.GET['name']
        rep = Reply.objects.filter(title__icontains=tit) | Reply.objects.filter(title__icontains=name)
        return render_to_response('search_results.html',
            {'rep': rep, 'query': tit})
    else:
        return render_to_response('search_form.html', {'error': True})

    if 'titl' in request.GET and request.GET['titl']:
        titl = request.GET['titl']
        req = Request.objects.filter(title__icontains=titl)
        return render_to_response('search_results.html',
            {'req': req, 'query': titl})
    else:
        return render_to_response('search_form.html', {'error': True})
