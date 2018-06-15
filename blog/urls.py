from django.conf.urls import url
from . import views

# "r'^$'" representa uma URL 'http://127.0.0.1:8000 /', onde entre o '0' e ' /' existe o espaço, pois a expressão regular não reconhece o '/'.
# Então, tudo o que está depois de 'http://127.0.0.1:8000' é vazio, por isso, quando o padrão identifica o vazio ele executa a 'views' e 'post_list'
# Então, quando o usuário digita 'http://127.0.0.1:8000 /', Django entende através de views.post_list que está no lugar correto
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

