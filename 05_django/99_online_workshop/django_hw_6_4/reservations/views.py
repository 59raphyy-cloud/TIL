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

def create(request):
    # 1. POST 방식일 때: 데이터 저장
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')
    
    # 2. GET 방식일 때 (또는 유효성 검사 실패 시)
    else:
        form = ReservationForm()
    
    # 폼을 담아서 템플릿 렌더링
    context = {'form': form}
    return render(request, 'reservations/create.html', context)
        
    
