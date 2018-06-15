# Por último, queremos uma forma legal de adicionar e editar as postagens do nosso blog. 
# Uma coisa legal do Django é que nós podemos tanto criar um formulário do zero como podemos criar um ModelForm que salva o resultado do formulário para um determinado modelo.
# Isso é exatamente o que nós queremos fazer: criaremos um formulário para o nosso modelo Post.
# Assim como toda parte importante do Django, os formulários tem seu próprio arquivo: forms.py.
# Precisamos criar um arquivo com este nome dentro da pasta blog.

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
