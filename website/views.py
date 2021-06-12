from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from website.forms import PostForm, CommentForm
from website.models import Post, Category, Tag, Author, Comment


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = Author.objects.all().get(user=request.user)
            form.save()

    context = {
        'form': PostForm()
    }
    return render(request, 'djProject/create.html', context=context)


class PostListView(ListView):
    model = Post
    paginate_by = 2

    def get_context_data(self, **kwargs):
        content = super(PostListView, self).get_context_data(**kwargs)
        content['odd_categories'] = Category.objects.all().order_by('name')[::2]
        content['even_categories'] = Category.objects.all().order_by('name')[1::2]
        content['odd_tags'] = Tag.objects.all().order_by('name')[::2]
        content['even_tags'] = Tag.objects.all().order_by('name')[1::2]
        return content


class PostDetailView(FormMixin, DetailView):
    model = Post
    paginate_by = 10

    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', args=[str(self.get_object().pk)])

    def get_context_data(self, **kwargs):
        content = super(PostDetailView, self).get_context_data(**kwargs)
        content['odd_tags'] = content['post'].tags.all()[::2]
        content['even_tags'] = content['post'].tags.all()[1::2]
        content['comments'] = Comment.objects.filter(post=content['post'])
        content['form'] = self.get_form()
        return content

    def get_initial(self):
        return {'event': self.get_object()}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and str(self.request.user) != 'AnonymousUser':  # TODO: Переделать
            print(type(self.request.user))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.created_by = self.request.user
        f.post = self.get_object()
        f.save()
        return super(PostDetailView, self).form_valid(form)


# class PostDetailView(generic.DetailView):
#     model = Post
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         content = super(PostDetailView, self).get_context_data(**kwargs)
#         content['odd_tags'] = content['post'].tags.all()[::2]
#         content['even_tags'] = content['post'].tags.all()[1::2]
#         content['comments'] = Comment.objects.filter(created_by=content['post'].author.user)# Перепроверить
#         content['form'] = CommentForm()
#         return content


class CategoryListView(ListView):
    model = Category
    paginate_by = 10


class CategoryDetailView(DetailView):
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        content = super(CategoryDetailView, self).get_context_data(**kwargs)
        content['all_post_category'] = Post.objects.filter(category=content['category']).order_by('created_at')
        return content


class TagListView(ListView):
    model = Tag
    paginate_by = 10


class TagDetailView(DetailView):
    model = Tag
    paginate_by = 10

    def get_context_data(self, **kwargs):
        content = super(TagDetailView, self).get_context_data(**kwargs)
        content['all_post_tag'] = Post.objects.filter(tags__in=[content['tag']]).order_by('created_at')
        return content


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author
    paginate_by = 10

    def get_context_data(self, **kwargs):
        content = super(AuthorDetailView, self).get_context_data(**kwargs)
        content['all_post_author'] = Post.objects.filter(author=content['author']).order_by('created_at')
        return content
