from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'director',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '영화 제목을 입력하세요'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }