from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm()
    context = {
        'author': author,
        'book_form': book_form,
    }
    return render(request, 'libraries/detail.html', context)

def create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
    return redirect('libraries:detail', author.pk)
