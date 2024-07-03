from django import forms
from story_fetcher.models import Tag
from .models import UserProfile

class UserPreferencesForm(forms.ModelForm):
    excluded_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ['excluded_tags']