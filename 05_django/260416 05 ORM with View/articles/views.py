from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 1. 전체 게시글 조회
# 2. DB로 부터 받은 전체 게시글 데이터를 변수에 담아
# 3. 템플릿과 함께 렌더링
def index(request):
    # 1~2 전체 게시글 조회
    articles = Article.objects.all()

    # 3. context에 게시글 데이터 담기
    context = {
        'articles': articles,
    }

    # 4. 메인 페이지와 함께 응답
    return render(request, 'articles/index.html', context)

# 1. URL로부터 넘겨받은 정수 값을 활용해 게시글을 조회
# 2. 조회된 단일 게시글 데이터를 변수에 담아
# 3. 페이지와 함께 렌더링
def detail(request, article_pk):
    # 1. 특정 게시글 조회
    article = Article.objects.get(pk=article_pk)

    # 2. context에 담아
    context = {
        'article': article,
    }

    # 3. 상세 페이지와 함께 응답
    return render(request, 'articles/detail.html', context)


# 게시글 작성을 위한 페이지를 응답
def new(request):
    return render(request, 'articles/new.html')

# 1. 클라이언트로 부터 받은 게시글 데이터를 추출
# 2. 추출한 데이터를 변수에 할당
# 3. 준비된 데이터를 DB에 저장 요청
# 4.1 잘 저장 되었습니다 라는 페이지 응답하기
# 4.2 클라이언트를 메인 페이지(상세 페이지)로 보내기
def create(request):
    # 1. 클라이언트 요청 객체안에서 제목과 내용 데이터를 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. Article 모델 클래스를 활용해서 저장을 진행
    # 2.1 저장 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.2 저장 두번째 방법
    article = Article(title=title, content=content)
    article.save()

    # 2.3 저장 세번째 방법
    # Article.objects.create(title=title, content=content)

    # 게시글이 잘 작성되었다는 문구가 작성된 페이지를 응답
    # return render(request, 'articles/create.html')

    # 사용자는 게시글을 작성해줘! 라고 요청했기 때문에
    # 페이지를 제공하는 것은 어색한 흐름
    # 게시글 작성이 마무리가 되고 클라이언트는 어디로 가야 자연스러울까?
    # 후보1. 메인페이지 / 후보2. 지금 막 작성한 게시글의 상세페이지
    # return redirect('클라이언트가 여기로 다시 요청을 보냈으면 하는 주소를 작성')
    
    # 후보1. 클라이언트에게 메인 페이지로 다시 요청을 보내! 라는 응답
    # return redirect('articles:index')

    # 후보2. 클라이언트에게 지금 막 작성된 게시글의 상세 페이지로 다시 요청을 보내! 라는 응답
    return redirect('articles:detail', article.pk)


# 1. url에서 넘어온 변수 값으로 어떤 게시글을 삭제해야 하는지를 먼저 조회
# 2. 조회된 게시글을 DB에 삭제 요청
def delete(request, article_pk):
    # 1. 특정 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 2. DB 삭제 요청
    article.delete()
    # 3. 삭제 이후에 어떤 과정이 자연스러운가? 삭제가 완료되었다라는 걸 보여주는 페이지?
    # 아니면 삭제 이후에 적절한 페이지로 갈 수 있도록 안내하는 것? 당연히 후자.
    return redirect('articles:index')

# 1. 수정 할 수 있는 페이지를 렌더링
# 2. 어떤 게시글을 수정하는지 조회
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


# 1. 사용자 입력 데이터를 추출하여 변수에 할당
# 2. 수정하고자하는 게시글을 조회
# 3. 추출한 데이터를 기반으로 기존 게시글의 데이터를 갱신
# 4. 갱신 준비가 완료된 새로운 데이터를 DB에 수정 요청
def update(request, article_pk):
    # 2. 
    article = Article.objects.get(pk=article_pk)
    
    # 1.
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 3. 
    article.title = title
    article.content = content

    # 4.
    article.save()

    return redirect('articles:detail', article.pk)