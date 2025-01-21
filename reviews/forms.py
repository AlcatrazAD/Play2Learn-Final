from django.forms import ModelForm, Textarea

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['submission']
        widgets = {
            'submission': Textarea(
                attrs={'cols': 20, 'rows': 6, 'autofocus': True}
            )
        }
        help_texts = {
            'submission': 'be nice'
        }