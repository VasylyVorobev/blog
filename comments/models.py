from django.contrib.auth.models import User
from django.db import models


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, verbose_name='Пост')
    created = models.DateTimeField('Создан', auto_now_add=True)
    text = models.TextField('Текст комментария')
    status = models.BooleanField('Удалить комментарий', default=False)

    def __str__(self):
        return f'Комментарий от {self.author.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-created', )

