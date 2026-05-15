from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, DailyLog, UserProfile
from .serializers import CategorySerializer, DailyLogSerializer, UserProfileSerializer


# ==========================================
# [F806] category_list 함수 구현
# 전체 관심사 카테고리 목록 조회
# ==========================================
@api_view(['GET'])
def category_list(request):
    """
    대분류/소분류 체계 전체를 반환 (초기 데이터 확인용)
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# ==========================================
# [F807] create_log 함수 구현
# 이미지 또는 텍스트 기반 TMI 로그 생성
# ==========================================
@api_view(['POST'])
def create_log(request):
    """
    이미지와 텍스트를 모두 처리하며, 유저의 입력에 따라 AI 로직 분기
    """
    serializer = DailyLogSerializer(data=request.data)
    
    if serializer.is_valid():
        # 데이터 저장 전 AI/NLP 처리를 위한 준비
        instance = serializer.save(user=request.user)
        
        # [분기 1] 이미지가 업로드된 경우
        if instance.image:
            # TODO: Vision AI 연동 (예: YOLO 모델 호출)
            instance.detected_object = "인식된 사물명" # 예: '텀블러'
            instance.tmi_content = "이 사물은 Wikipedia에 따르면... (GPT 요약)"
        
        # [분기 2] 텍스트만 입력된 경우
        elif instance.raw_text:
            # TODO: NLP 키워드 추출 로직 연동
            instance.detected_object = "Text Input"
            instance.tmi_content = "입력하신 글을 바탕으로 분석한 TMI입니다."
            
        instance.save() # 가공된 데이터 최종 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# [F808] log_list 함수 구현
# 전체 TMI 로그 목록 조회
# ==========================================
@api_view(['GET'])
def log_list(request):
    """
    모든 사용자의 로그를 최신순으로 반환
    """
    logs = DailyLog.objects.all() # 모델의 Meta 클래스에 ordering=["-created_at"]이 있어 자동 정렬됨
    serializer = DailyLogSerializer(logs, many=True)
    return Response(serializer.data)


# ==========================================
# [F809] log_detail 함수 구현
# 단일 TMI 로그 조회, 수정, 삭제
# ==========================================
@api_view(['GET', 'PUT', 'DELETE'])
def log_detail(request, log_pk):
    """
    특정 로그의 상세 내용을 확인하거나, 작성자가 내용을 수정/삭제함
    """
    log = get_object_or_404(DailyLog, pk=log_pk)

    # [조회] 특정 로그의 전체 필드 반환
    if request.method == 'GET':
        serializer = DailyLogSerializer(log)
        return Response(serializer.data)

    # [수정] 로그의 설명이나 텍스트 등을 수정 (작성자 본인 확인 로직 권장)
    elif request.method == 'PUT':
        serializer = DailyLogSerializer(log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # [삭제] 로그 삭제
    elif request.method == 'DELETE':
        log.delete()
        return Response({'message': '로그가 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


# ==========================================
# [F810] user_profile_detail 함수 구현
# 유저 프로필 조회 및 관심사 수정
# ==========================================
@api_view(['GET', 'PUT'])
def user_profile_detail(request):
    """
    로그인한 유저 본인의 프로필과 관심사(interests) 목록을 관리
    (URL에 ID를 넣기보다 request.user를 사용하는 것이 보안상 안전함)
    """
    # User와 1:1 연결된 프로필 가져오기
    profile = get_object_or_404(UserProfile, user=request.user)

    # [조회] 내 프로필과 등록한 관심사 확인
    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    # [수정] 관심사 카테고리 업데이트
    elif request.method == 'PUT':
        # interests 필드에 카테고리 ID 리스트를 보내면 ManyToMany 관계가 업데이트됨
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

