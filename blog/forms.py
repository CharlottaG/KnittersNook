from .models import Comment, Pattern
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ['pattern_name', 'description', 'featured_image', 'difficulity_level', 'needle_size', 'yarn', 'gauge']