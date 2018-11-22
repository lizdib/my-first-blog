from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Reply
from .models import Request

def post_list(request):
    posts1 = Reply.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts2 = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts1})
    return render(request, 'blog/post_list.html', {'posts': posts2})
