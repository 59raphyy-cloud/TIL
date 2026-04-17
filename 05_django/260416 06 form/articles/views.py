from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    # ModelForm을 적용한 저장 과정
    # 1. 모델 폼이 사용자 입력 데이터를 모두 다 받음
    article_form = ArticleForm(request.POST)  # 위의 new에서 사용한 인스턴스와 다름. 데이터를 받은 인스턴스

    # 2. 유효성 검사
    if article_form.is_valid():  # 상속받은 모델폼 클래스(ArticleForm이 제공해주는 메서드)
        # 2-1. 유효성 검사를 통과했다면 저장
        #   모델폼의 save 메서드는 생성된 객체를 반환함
        article = article_form.save()
        # 2-2. 저장 이후에는 상세페이지로 리다이렉트
        return redirect('articles:detail', article.pk)
    
    # 3. 통과하지 못했다면, 이유(에러메시지)와 함께 페이지 다시 제공
    #    is_valid를 통과하지 못한 form 인스턴스에는 통과하지 못한 이유가 담겨있음
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)
    
    
    
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title=title, content=content)
    # article.save()

    return redirect('articles:detail', article.pk)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect('articles:detail', article.pk)