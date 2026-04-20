from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # upload_to의 경로는 'MEDIA_ROOT 경로' 이후의 경로로 설정됨
    # 실제 DB에 저장될 때는 'images/sample.png' 이런 문자열이 저장됨
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)