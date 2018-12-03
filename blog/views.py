from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from .forms import ReplyForm
from .forms import RequestForm
from .forms import Reply_registerForm
from .forms import Request_registerForm
from .models import Reply
from .models import Request
from .models import Reply_register
from .models import Request_register
from django.db.models import Q

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

def Reply_new(request):
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            Reply = form.save(commit=False)
            Reply.author = request.user
            Reply.save()
            return redirect('Reply_detail', pk=Reply.pk)
    else:
        form = ReplyForm()
    return render(request, 'blog/Reply_edit.html', {'Reply': form})

def Reply_edit(request, pk):
    rep = get_object_or_404(Reply, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=rep)
        if form.is_valid():
            rep = form.save(commit=False)
            rep.author = request.user
            rep.save()
            return redirect('Reply_detail', pk=Reply.pk)
    else:
        form = ReplyForm(instance=rep)
    return render(request, 'blog/Reply_edit.html', {'Reply': form})

def Request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            Request = form.save(commit=False)
            Request.author = request.user
            Request.save()
            return redirect('Request_detail', pk=Request.pk)
    else:
        form = RequestForm()
    return render(request, 'blog/Request_edit.html', {'Request': form})

def Request_edit(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            req = form.save(commit=False)
            req.author = request.user
            req.save()
            return redirect('Request_detail', pk=Request.pk)
    else:
        form = RequestForm(instance=req)
    return render(request, 'blog/Request_edit.html', {'Request': form})

def Reply_remove(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    reply.delete()
    return HttpResponseRedirect("/")

def Request_remove(request, pk):
    req = get_object_or_404(Request, pk=pk)
    req.delete()
    return HttpResponseRedirect("/")

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 't' in request.GET and request.GET['t']:
        t = request.GET['t']
        requests = Request.objects.filter(Q(id=t)|Q(name_of_inhabitant=t)|
        Q(phone_number=t)|Q(email=t)|Q(reason=t))
        replies = Reply.objects.filter(Q(id=t)|Q(name_of_inhabitant=t)|Q(result=t))
        repreg = Reply_register.objects.filter(Q(title=t)|Q(reply_number=t)|Q(name_of_inhabitant=t)|
        Q(result=t)|Q(name_of_doer=t)|Q(request_status=t))
        reqreg = Request_register.objects.filter(Q(title=t)|Q(request_number=t)|Q(name_of_inhabitant=t)|Q(phone_number=t)|Q(email=t)|
        Q(reason=t)|Q(name_of_doer=t)|Q(request_status=t))
        return render_to_response('search_results.html',
            {'Requests': requests, 'Replies': replies, 'Reply_register': repreg, 'Request_register': reqreg, 'query': t})
    else:
        return render_to_response('search_form.html', {'error': True})
