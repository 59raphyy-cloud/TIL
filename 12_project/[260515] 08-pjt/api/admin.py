from django.contrib import admin
from .models import Category, UserProfile, DailyLog

# 1. 카테고리: 대분류/소분류를 한눈에 보게 설정
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_category', 'sub_category')
    list_filter = ('parent_category',) # 대분류별로 필터링해서 보기 편함
    search_fields = ('sub_category',)

# 2. 유저 프로필: 연결된 유저명 확인
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

# 3. 데일리 로그: 이미지 미리보기 기능 포함 (선택 사항)
@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'detected_object', 'created_at', 'get_image')
    readonly_fields = ('get_image',) # 관리자 페이지에서 이미지를 볼 수 있게 함

    def get_image(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="50px" />')
        return "No Image"
    get_image.short_description = '미리보기'