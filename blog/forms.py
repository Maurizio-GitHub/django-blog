from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # All we are doing here is telling our CommentForm
    # what model to use and, then, which fields we want
    # displayed on our form (in this case, 'body'):
    class Meta:
        model = Comment
        fields = ('body',)
