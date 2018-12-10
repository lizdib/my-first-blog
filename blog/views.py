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
from django.db.models import Q, Count
from datetime import datetime, date, time
from django.contrib.auth.decorators import login_required

@login_required
def Request_list(request):
    req = Request.objects.order_by('id')
    podate = Request.objects.filter(created_date__year='2018').filter(created_date__month='12')
    count = Request.objects.count()
    return render(request, 'show_requests.html', {'req': req, 'podate': podate, 'count': count})

@login_required
def Reply_list(request):
    rep = Reply.objects.order_by('id')
    count = Reply.objects.count()
    return render(request, 'show_replies.html', {'rep': rep, 'count': count})

@login_required
def Request_register_list(request):
    reqreg = Request_register.objects.order_by('title')
    return render(request, 'show_request_register.html', {'reqreg': reqreg})

@login_required
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

@login_required
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

@login_required
def Reply_edit(request, pk):
    rep = get_object_or_404(Reply, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=rep)
        if form.is_valid():
            rep = form.save(commit=False)
            rep.author = request.user
            rep.save()
            return redirect('Reply_detail', pk=rep.pk)
    else:
        form = ReplyForm(instance=rep)
    return render(request, 'blog/Reply_edit.html', {'Reply': form})

@login_required
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

@login_required
def Request_edit(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            req = form.save(commit=False)
            req.author = request.user
            req.save()
            return redirect('Request_detail', pk=req.pk)
    else:
        form = RequestForm(instance=req)
    return render(request, 'blog/Request_edit.html', {'Request': form})

@login_required
def Reply_remove(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    reply.delete()
    return HttpResponseRedirect("/")

@login_required
def Request_remove(request, pk):
    req = get_object_or_404(Request, pk=pk)
    req.delete()
    return HttpResponseRedirect("/")

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 't' in request.GET and request.GET['t']:
        t = request.GET['t']
        requests = Request.objects.filter(Q(id__iexact=t)|Q(name_of_inhabitant__iexact=t)|
        Q(phone_number=t)|Q(email__iexact=t)|Q(reason=t))
        replies = Reply.objects.filter(Q(id__iexact=t)|Q(name_of_inhabitant__iexact=t)|Q(result=t))
        repreg = Reply_register.objects.filter(Q(title__iexact=t)|Q(reply_number=t)|Q(name_of_inhabitant__iexact=t)|
        Q(result__iexact=t)|Q(name_of_doer=t)|Q(request_status=t))
        reqreg = Request_register.objects.filter(Q(title__iexact=t)|Q(request_number=t)|Q(name_of_inhabitant__iexact=t)|Q(phone_number=t)|Q(email__iexact=t)|
        Q(reason__iexact=t)|Q(name_of_doer=t)|Q(request_status=t))
        requests1 = Request.objects.filter(Q(id__iexact=t)|Q(name_of_inhabitant__iexact=t)|
        Q(phone_number=t)|Q(email__iexact=t)|Q(reason=t)).count()
        kolvo1 = int(requests1)
        replies1 = Reply.objects.filter(Q(id__iexact=t)|Q(name_of_inhabitant__iexact=t)|Q(result=t)).count()
        kolvo2 = int(replies1)
        repreg1 = Reply_register.objects.filter(Q(title__iexact=t)|Q(reply_number=t)|Q(name_of_inhabitant__iexact=t)|
        Q(result__iexact=t)|Q(name_of_doer=t)|Q(request_status=t)).count()
        kolvo3 = int(repreg1)
        reqreg1 = Request_register.objects.filter(Q(title__iexact=t)|Q(request_number=t)|Q(name_of_inhabitant__iexact=t)|Q(phone_number=t)|Q(email__iexact=t)|
        Q(reason__iexact=t)|Q(name_of_doer=t)|Q(request_status=t)).count()
        kolvo4 = int(reqreg1)
        return render_to_response('search_results.html',
            {'requests': requests, 'replies': replies, 'repreg': repreg, 'reqreg': reqreg, 'kolvo1':kolvo1, 'kolvo2':kolvo2, 'kolvo3':kolvo3, 'kolvo4':kolvo4, 'query': t})
    else:
        return render_to_response('search_form.html', {'error': True})
