from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 1. 전체 목록 확인
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 2. 생성 폼 보여주기
def new(request):
    return render(request, 'articles/new.html')

# 3. 데이터 저장 및 리다이렉트
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:index')