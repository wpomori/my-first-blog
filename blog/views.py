from django.shortcuts import render

# A função '(def)' chamada 'post_list' que recebe um 'request' e retorna '(return)' uma função 'render', que irá renderizar (montar) o modelo 'blog/post_list.html'.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

