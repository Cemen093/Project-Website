from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Фамилия')
    login = models.CharField(max_length=100, null=False, blank=False, verbose_name='Логин')
    image = models.ImageField(upload_to='author/', null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.id)])


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.TextField(null=False, blank=False, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Обновлен')
    published = models.BooleanField(null=False, verbose_name='Опубликован')
    author = models.ForeignKey(Author, null=False, on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey(Category, null=False, on_delete=models.PROTECT, verbose_name='Категории')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    image = models.ImageField(upload_to='post/', null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    description = models.TextField(null=False, blank=False, verbose_name='Текст сообщения')

    def __str__(self):
        return 'Created by {} in {}'.format(self.created_by.last_name, self.created_at.date())
