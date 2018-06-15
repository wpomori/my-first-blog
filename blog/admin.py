from django.contrib import admin
# Aqui vamos importar o modelo 'Post' definido em 'blog/models.py'
from .models import Post

# Após a importação de 'Post', precisamos torná-lo visível na nossa página.
# Por isso, precisamos registrá-lo
admin.site.register(Post)

