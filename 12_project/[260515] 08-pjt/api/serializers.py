from rest_framework import serializers
from .models import Category, UserProfile, DailyLog

# ==========================================
# [F805] Serializer 클래스 구현
# ==========================================

# 1. 카테고리 정보 전송용
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# 2. TMI 로그 생성 및 상세 조회용
class DailyLogSerializer(serializers.ModelSerializer):
    # 읽기 전용 필드들 (조회할 때만 보이고 생성 시에는 수동 입력 안 함)
    user_username = serializers.ReadOnlyField(source='user.username')
    matched_category_name = serializers.ReadOnlyField(source='matched_category.sub_category')

    class Meta:
        model = DailyLog
        fields = [
            'id', 'user_username', 'image', 'raw_text', 
            'detected_object', 'matched_category', 'matched_category_name', 
            'tmi_content', 'created_at'
        ]
        # tmi_content나 detected_object는 AI가 채울 것이므로 읽기 전용 처리 가능
        read_only_fields = ['tmi_content', 'detected_object']

# 3. 유저 프로필 및 관심사 수정용
class UserProfileSerializer(serializers.ModelSerializer):
    # ManyToMany 관계인 관심사들을 이름으로 보여주기 위한 설정
    interests_detail = CategorySerializer(many=True, read_only=True, source='interests')
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'interests', 'interests_detail']