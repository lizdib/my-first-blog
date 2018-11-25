from django.shortcuts import render, get_object_or_404
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
