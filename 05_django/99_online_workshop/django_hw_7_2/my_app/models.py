from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    # 사용자가 업로드 한 파일의 저장 위치를 '/uploaded_files/' 폴더로 지정
    image = models.ImageField(upload_to='uploaded_files/', blank=True)