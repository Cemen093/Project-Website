from django import forms

from website.models import Post, Author, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = 'created_at', 'updated_at', 'author'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = 'created_at', 'created_by', 'post'
