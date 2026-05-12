from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # 저자 객체는 사용자가 직접 선택하지 않도록 제외
        exclude = ('author',)