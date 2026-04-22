from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

# 예약 생성 페이지
def new(request):
    form = ReservationForm()
    context = {'form': form}
    return render(request, 'reservations/new.html', context)

# 실제 데이터 저장 처리
def create(request):
    # POST로 넘어온 데이터를 ModelForm에 담습니다.
    form = ReservationForm(request.POST)
    
    # 유효성 검사
    if form.is_valid():
        form.save() # 통과하면 바로 DB에 저장
        return redirect('reservations:index')
    
    # 만약 유효하지 않다면, 에러 메시지를 포함한 폼을 다시 보여줌
    context = {'form': form}
    return render(request, 'reservations/new.html', context)