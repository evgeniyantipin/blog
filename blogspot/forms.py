from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        labels = {'name': 'Имя', 'body': 'Комментарий'}
        exclude = ['post']
