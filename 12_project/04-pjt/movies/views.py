from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie
from .forms import MovieForm
from .utils import get_ai_director_info

# Create your views here.
@require_safe
def index(request):
    # DB에서 모든 영화 데이터를 가져옴
    # .order_by('-pk'): 최신 등록순 정렬
    movies = Movie.objects.all().order_by('-pk')
    # 데이터를 템플릿으로 넘겨주기 위해 context에 담음
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(["GET", "POST"])
def create(request):
    # POST 요청: 사용자가 데이터를 써서 보냈을 때
    if request.method == 'POST':
        form = MovieForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # commit=False로 설정하여 DB에 바로 저장하지 않고 대기
            movie = form.save(commit=False)

            # 사용자가 입력한 감독 이름을 가져와 AI 함수 실행
            try:
                img, info, works = get_ai_director_info(movie.director)
                
                # AI가 가져온 데이터를 비어있는 필드에 할당
                movie.director_img_url = img
                movie.director_info = info
                movie.director_works = works
            except Exception as e:
                # AI 호출 실패 시 로그를 남기거나 기본값을 넣음
                print(f"AI 호출 에러: {e}")
            
            # 모든 정보가 채워졌으므로 최종 저장
            movie.save()

            # 저장 후 상세 페이지로 리다이렉트
            return redirect('movies:detail', movie.pk)
    
    # GET 요청: 사용자가 처음 페이지에 들어왔을 때
    else:
        form = MovieForm()
    
    # 유효성 검사에 실패했거나 GET 요청일 경우
    # form 객체는 에러 메시지를 포함하고 있어 템플릿에서 자동으로 에러를 보여줌
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, pk):
    # pk에 해당하는 영화를 가져옴
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    # 수정 대상이 되는 영화 데이터를 가져옴
    movie = Movie.objects.get(pk=pk)
    
    if request.method == 'POST':
        # POST 요청: 사용자가 수정한 데이터를 기존 인스턴스(movie)에 덮어씀
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            # 수정 후 상세 페이지로 리다이렉트
            return redirect('movies:detail', movie.pk)
    else:
        # GET 요청: 기존 영화 데이터가 미리 입력된 폼을 UI로 제공
        form = MovieForm(instance=movie)
    
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, pk):
    # 삭제할 데이터를 찾음
    movie = Movie.objects.get(pk=pk)
    # 데이터 삭제
    movie.delete()
    # 삭제 후 목록 페이지(index)로 리다이렉트
    return redirect('movies:index')
