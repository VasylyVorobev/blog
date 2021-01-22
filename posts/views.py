from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category
from .mixins import CustomSuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from comments.forms import CommentForm


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    paginate_by = 4


class PostDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = CommentForm
    success_msg = 'Комментарий добавлен'

    def get_success_url(self, **kwargs):
        return reverse_lazy('posts:post_detail_url', kwargs={'slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)


class CategoryListView(View):

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        queryset = Post.objects.filter(category_id=category_id)
        return render(request, 'posts/category_list.html', {'objects': queryset, 'category': category})


class PostCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = Post
    fields = ('title', 'img', 'description', 'category')
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:post_list_url')
    success_msg = 'Пост успешно создан'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Post
    fields = ('title', 'img', 'description', 'category')
    template_name = 'posts/post_update.html'
    success_url = reverse_lazy('posts:post_list_url')
    success_msg = 'Пост успешно обновлен'

    def get_form_kwargs(self):
        kwargs = super(PostUpdateView, self).get_form_kwargs()
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_detail.html'
    success_url = reverse_lazy('posts:post_list_url')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Пост удален')
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
