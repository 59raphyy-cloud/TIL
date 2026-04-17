from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    director = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 감독 정보 추가 필드
    director_img_url = models.URLField(blank=True, null=True)  # 프로필 이미지 링크
    director_info = models.TextField(blank=True, null=True)    # 감독 설명
    director_works = models.JSONField(blank=True, null=True)   # 대표작 목록 (리스트 형태 저장)

    # 관리자 페이지나 shell에서 데이터가 제목으로 보이게 설정
    def __str__(self):
        return self.title