from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 반드시 POST 방식일 때만 삭제 수행
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')  # 삭제 후 목록으로 리다이렉트
    else:
        # 주소창에 직접 입력해서(GET) 들어오면 상세 페이지로 다시 보냄
        return redirect('articles:detail', article.pk)