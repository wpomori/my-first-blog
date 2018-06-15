from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # Note que os métodos (def) estão indentados dentro da classe
    # Como Python é sensível a espaços, isto define o relacionamento entre a classe 'Post' e os métodos 'def'
    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

