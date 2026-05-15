from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# ==========================================
# [F802] Category 클래스 구현
# 마스터 데이터 - 관심사 카테고리 모델
# ==========================================
class Category(models.Model):
    """
    서비스에서 제공하는 표준 관심사 분류 체계
    초기 Fixture 데이터(initial_categories.json)를 통해 DB에 선진입됨
    """

    parent_category = models.CharField(
        max_length=50, help_text="대분류 (예: IT/기술, 인문/역사)"
    )
    sub_category = models.CharField(
        max_length=50, help_text="소분류 관심사 (예: 반도체, 요리)"
    )

    class Meta:
        verbose_name = "관심사 카테고리"
        verbose_name_plural = "관심사 카테고리 목록"
        # 중복 데이터 처리
        constraints = [
            models.UniqueConstraint(fields=['parent_category', 'sub_category'], name='unique_category')
        ]

    def __str__(self):
        return f"[{self.parent_category}] {self.sub_category}"


# ==========================================
# [F803] UserProfile 클래스 구현
# 사용자 데이터 - 확장형 유저 프로필 모델
# ==========================================
class UserProfile(models.Model):
    """
    기존 Auth User 모델과 1:1 매핑되어 확장된 유저 정보 관리
    사용자가 회원가입 시 설정한 다중 관심사(소분류)를 저장함
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    # 한 사용자가 여러 소분류를 고를 수 있고, 한 소분류가 여러 사용자에게 선택됨 (N:M)
    interests = models.ManyToManyField(
        Category, related_name="interested_users", blank=True
    )

    def __str__(self):
        return f"{self.user.username}의 프로필"


# ==========================================
# [F804] DailyLog 클래스 구현
# 로그 데이터 - 핵심 일상 기록 및 TMI 로그 모델
# ==========================================
class DailyLog(models.Model):
    """
    유저가 사진을 업로드한 순간의 스냅숏 데이터 저장
    실시간으로 AI 엔진 및 Wikipedia API, GPT Nano를 거쳐 가공된 최종 TMI만 적재
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="daily_logs"
    )
    
    # 텍스트 입력을 위한 필드
    raw_text = models.TextField(null=True, blank=True, help_text="사용자가 직접 입력한 일상 텍스트")
    
    # 이미지 파일이 물리적으로 저장될 경로 (%Y/%m/%d 구조로 일자별 자동 분류 저장)
    image = models.ImageField(upload_to="logs/%Y/%m/%d/", null=True, blank=True)

    # 1단계 Vision Engine: AI(YOLO)가 사진에서 추출한 객체 레이블명 (예: '컴퓨터')
    detected_object = models.CharField(
        max_length=50, null=True, blank=True, help_text="AI 비전 엔진이 인식한 물체 이름"
    )

    # 2단계 Logic: 유저의 관심사 중 이 사진의 키워드와 매칭되어 사용된 소분류 카테고리
    matched_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="TMI 컨텍스트 매칭에 사용된 유저의 관심사 소분류",
    )

    # 3단계 NLP Engine: Wikipedia API 원문을 GPT Nano로 실시간 압축한 핵심 TMI 데이터 ⭐
    tmi_content = models.TextField(blank=True, null=True, help_text="실시간으로 요약된 사용자 맞춤형 2줄 TMI")

    created_at = models.DateTimeField(auto_now_add=True, help_text="기록 생성 일시")
    
    # 데이터 무결성 검사
    def clean(self):
        if not self.image and not self.raw_text:
            raise ValidationError("텍스트 또는 이미지를 입력해주세요.")

    class Meta:
        ordering = ["-created_at"]  # 최신 로그가 가장 먼저 보이도록 정렬

    def __str__(self):
        return f"{self.user.username}의 로그 ({self.detected_object})"

