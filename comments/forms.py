from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {'text': forms.Textarea(attrs={'rows': 5})}
