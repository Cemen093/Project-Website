from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views
from .views import create

urlpatterns = [
    # path('', index, name='index'),
    # path('post/<int:pk>/', details, name='details'),
    path('create/', create, name='create'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^categories/$', views.CategoryListView.as_view(), name='categories'),
    url(r'^category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'^tags/$', views.TagListView.as_view(), name='tags'),
    url(r'^tag/(?P<pk>\d+)$', views.TagDetailView.as_view(), name='tag-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
