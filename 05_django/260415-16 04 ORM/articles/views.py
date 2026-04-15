from django.shortcuts import render
from .models import Article

# Create your views here.
# 1. 전체 게시글 조회
# 2. DB로부터 받은 전체 게시글 데이터를 변수에 담아
# 3. 템플릿과 함께 렌더링
def index(request):
    # 1~2. 전체 게시글 조회 요청
    articles = Article.objects.all()

    # 3. context에 게시글 데이터 담기
    context = {
        'articles': articles,
    }

    # 4. 메인 페이지와 함께 응답
    return render(request, 'articles/index.html', context)


# 1. URL로부터 넘겨받은 정수 값을 활용해 게시글 조회
# 2. 조회된 단일 게시글 데이터를 변수에 담고
# 3. 페이지와 함께 렌더링
def detail(request, article_pk):
    # 1. 특정 게시글 조회
    article = Article.objects.get(pk=article_pk)

    # 2. context에 담음
    context = {
        'article': article,
    }

    # 3. 상세 페이지와 함께 응답
    return render(request. 'articles/detail.html', context)


# 게시글 작성을 위한 페이지를 응답
def new(request):
    return render(request, 'articles/new.html')


# 1. 클라이언트로부터 받은 게시글 데이터 추출
# 2. 추출한 데이터를 변수에 할당
# 3. 준비된 데이터를 DB에 저장 요청
# 4-1. 잘 저장되었습니다 라는 페이지 응답
# 4-2. 클라이언트를 메인페이지(상세페이지)로 보냄 -> 얘가 훨씬 자연스러운 흐름
def create(request):
    # 1. 클라이언트 요청 객체 안에서 제목과 내용 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. Article 모델 클래스를 활용해서 저장 진행
    # 2-1. 저장 첫 번째 방법 -> 탈락2
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2-2. 저장 두 번째 방법
    article = Article(title=title, content=content)
    article.save()

    # 2-3. 저장 세 번째 방법 -> 탈락1
    # Article.objects.create(title=title, content=content)