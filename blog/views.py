from django.shortcuts import render
from django.utils import timezone
from .models import Post

# A função '(def)' chamada 'post_list' que recebe um 'request' e retorna '(return)' uma função 'render', que irá renderizar (montar) o modelo 'blog/post_list.html'.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


