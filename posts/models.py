from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from pytils.translit import slugify


def gen_slug(slug):
    return slugify(slug)


class Category(models.Model):
    title = models.CharField('Категория', max_length=40)
    slug = models.SlugField('Слаг', max_length=40)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField('Название поста', max_length=60)
    slug = models.SlugField('Слаг', max_length=60)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    img = models.ImageField('Изображение', upload_to='post_img/')
    description = models.TextField('Описание')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self, **kwargs):
        return reverse('posts:post_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created', )


