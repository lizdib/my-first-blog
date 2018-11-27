from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .forms import ReplyForm
from .forms import RequestForm
from .models import Reply
from .models import Request

def Request_list(request):
    req = Request.objects.filter(published_date__lte=timezone.now()).order_by('title1')
    return render(request, 'blog/post_list.html', {'req': req})

def Reply_list(request):
    rep = Reply.objects.filter(published_date__lte=timezone.now()).order_by('title')
    return render(request, 'blog/post_list.html', {'rep': rep})

def Request_detail(request, pk):
    req = get_object_or_404(Request, pk=pk)
    return render(request, 'blog/Request_detail.html', {'Request': req})

def Reply_detail(request, pk):
    rep = get_object_or_404(Reply, pk=pk)
    return render(request, 'blog/Reply_detail.html', {'Reply': rep})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        rep = Reply.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'rep': rep, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        req = Request.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'req': req, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})
