from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Reply
from .models import Request

def post_list(request):
    posts1 = Reply.objects.filter(published_date__lte=timezone.now()).order_by('title')
    posts2 = Request.objects.filter(published_date__lte=timezone.now()).order_by('title1')
    return render(request, 'blog/post_list.html', {'posts': posts1})
    return render(request, 'blog/post_list.html', {'posts': posts2})

def Reply_detail(request, pk):
    post = get_object_or_404(Reply, pk=pk)
    return render(request, 'blog/Reply_detail.html', {'Reply': post})

def Request_detail(request, pk):
    post = get_object_or_404(Request, pk=pk)
    return render(request, 'blog/Request_detail.html', {'Request': post})
